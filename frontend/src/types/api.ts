/**
 * API型定義
 */

export interface DocumentSiteProperty {
  id: string;
  document_type: string;
  url: string;
  description: string | null;
  created_at?: string;
  updated_at?: string;
}

export interface DocumentPagesResponse {
  page_count: number;
  targets: DocumentSiteProperty[];
}

export interface DocumentSiteCrawlingCondition {
  site_property_id: string;
  crawl_interval_minutes: number;
  is_active: boolean;
  created_at: string;
  updated_at: string;
}

export interface CrawlingTargetsResponse {
  page_count: number;
  targets: DocumentSiteCrawlingCondition[];
}

export interface AddCrawlingTargetRequest {
  site_id: string;
  crawl_interval: number;
}

export interface DeleteTargetResponse {
  message: string;
}

export interface ApiError {
  detail: string;
}
