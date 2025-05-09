##############################
# Stage 1: Build frontend
##############################
FROM node:22.15-alpine AS frontend-build

WORKDIR /app/frontend

# Copy frontend files
COPY frontend/package.json frontend/package-lock*.json* ./

# Install dependencies
RUN npm ci

# Copy the rest of the frontend code
COPY frontend/ ./

# Build frontend
RUN npm run build

##############################
# Stage 2: Build backend
##############################
FROM python:3.12-slim AS backend-build

WORKDIR /app/backend

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY backend/requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

##############################
# Stage 3: Final image
##############################
FROM python:3.12-slim

# Install Nginx and Supervisor
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx \
    supervisor \
    && rm -rf /var/lib/apt/lists/*

# Create app directories
WORKDIR /app
RUN mkdir -p /app/frontend /app/backend

# Copy frontend build from stage 1
COPY --from=frontend-build /app/frontend/dist /app/frontend

# Copy backend from stage 2
COPY --from=backend-build /app/backend /app/backend

# Install Python dependencies
WORKDIR /app/backend
RUN pip install --no-cache-dir -r requirements.txt

# Configure Nginx
COPY <<EOF /etc/nginx/conf.d/default.conf
server {
    listen 80;
    server_name localhost;

    # Serve frontend static files
    location / {
        root /app/frontend;
        index index.html;
        try_files \$uri \$uri/ /index.html;
    }

    # Proxy API requests to FastAPI backend
    location /api/ {
        proxy_pass http://localhost:8000/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Make sure the default nginx site is disabled
RUN rm -f /etc/nginx/sites-enabled/default || true

# Configure supervisor to run both Nginx and FastAPI
COPY <<EOF /etc/supervisor/conf.d/supervisord.conf
[supervisord]
nodaemon=true
user=root

[program:nginx]
command=nginx -g 'daemon off;'
autostart=true
autorestart=true
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0

[program:fastapi]
command=fastapi run --workers 4
directory=/app/backend
autostart=true
autorestart=true
stdout_logfile=/dev/stdout
stdout_logfile_maxbytes=0
stderr_logfile=/dev/stderr
stderr_logfile_maxbytes=0
EOF

# Create non-root user for better security
RUN groupadd -r appuser && useradd --no-log-init -r -g appuser appuser \
    && chown -R appuser:appuser /app

# Switch to non-root user for runtime (commented out for now as it might need elevated permissions)
# USER appuser

# Expose port
EXPOSE 80

# Start supervisor to manage processes
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]