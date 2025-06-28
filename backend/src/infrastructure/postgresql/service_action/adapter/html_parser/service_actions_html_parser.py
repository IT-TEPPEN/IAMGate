from html.parser import HTMLParser


class TableReader:
    def __init__(self):
        self.col_index = -1
        self.row_index = -1
        self.rowspan = 1
        self.colspan = 1
        self.cells = {}

    def create_row(self):
        self.col_index = 0
        self.row_index += 1

        if self.row_index not in self.cells:
            self.cells[self.row_index] = {}

    def create_cell(self, rowspan=1, colspan=1):
        self.col_index += colspan

        while True:
            if self.col_index in self.cells[self.row_index]:
                self.col_index += 1
            else:
                break

        self.rowspan = rowspan
        self.colspan = colspan

        for r in range(self.row_index, self.row_index + rowspan):
            if r not in self.cells:
                self.cells[r] = {}

            self.col_index = len(self.cells[r])

            for c in range(self.col_index, self.col_index + colspan):
                if c not in self.cells[r]:
                    self.cells[r][c] = {}

    def add_data(self, data):
        for r in range(self.row_index, self.row_index + self.rowspan):
            for c in range(self.col_index, self.col_index + self.colspan):
                if "data" not in self.cells[r][c]:
                    self.cells[r][c]["data"] = data
                else:
                    self.cells[r][c]["data"] += f",{data}"

    def add_link(self, link):
        for r in range(self.row_index, self.row_index + self.rowspan):
            for c in range(self.col_index, self.col_index + self.colspan):
                self.cells[r][c]["link"] = link

    def get_cells(self):
        result = []
        for r in range(self.row_index + 1):
            row = []
            for c in range(self.col_index + 1):
                cell = self.cells[r].get(c, {})
                data = cell.get("data", "")
                link = cell.get("link", "")
                row.append(
                    {
                        "data": data,
                        "url": link,
                    }
                )
            result.append(row)
        return result


class IAMServiceActionHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.table_reader = TableReader()
        self.in_table = False
        self.in_action_table = False
        self.in_th = False
        self.in_cell = False
        self.rows = []
        self.in_code = False  # Track if inside <code class="code">
        self.service_name = None
        self.service_prefix = None  # Store extracted service prefix
        self._in_p = False  # Track if inside <p>
        self._p_text = ""  # Buffer for <p> text
        self._pending_code_capture = False  # Flag to capture code as service prefix

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.in_table = True
        if tag == "th":
            self.in_th = True
        if self.in_table and self.in_action_table and tag == "tr":
            self.table_reader.create_row()
        if self.in_table and self.in_action_table and tag == "td":
            self.in_cell = True
            rowspan = 1
            colspan = 1
            for attr in attrs:
                if attr[0] == "rowspan":
                    rowspan = int(attr[1])
                if attr[0] == "colspan":
                    colspan = int(attr[1])
            self.table_reader.create_cell(rowspan=rowspan, colspan=colspan)
        if self.in_table and self.in_action_table and tag == "a":
            link = attrs[0][1] if attrs else ""
            self.table_reader.add_link(link)
        if tag == "p":
            self._in_p = True
            self._p_text = ""
        # Detect <code class="code"> inside <p> and after 'service prefix'
        if tag == "code":
            for attr in attrs:
                if attr[0] == "class" and attr[1] == "code":
                    self.in_code = True
                    if self._in_p and "service prefix" in self._p_text.lower():
                        self._pending_code_capture = True

                        if self.service_name is None:
                            self.service_name = self._p_text.split("(service prefix")[
                                0
                            ].strip()

    def handle_endtag(self, tag):
        if tag == "table":
            if self.in_action_table:
                self.rows = self.table_reader.get_cells()
            self.in_table = False
            self.in_action_table = False
        if tag == "th":
            self.in_th = False
        if tag == "td":
            self.in_cell = False
        if tag == "code":
            self.in_code = False
        if tag == "p":
            self._in_p = False
            self._p_text = ""
            self._pending_code_capture = False

    def handle_data(self, data):
        if self.in_th:
            if data.strip().lower() == "action" or data.strip().lower() == "actions":
                self.in_action_table = True
        if self.in_table and self.in_cell and data.strip() and data != " ":
            self.table_reader.add_data(data.strip())
        if self._in_p:
            self._p_text += data
        # Extract service prefix from <code class="code"> inside <p> after 'service prefix'
        if self.in_code and self._pending_code_capture and self.service_prefix is None:
            self.service_prefix = data.strip()
            self._pending_code_capture = False
