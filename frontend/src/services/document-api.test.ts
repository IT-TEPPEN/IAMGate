/**
 * documentApiのテスト
 */

import { describe, it, expect, beforeEach, vi } from "vitest";
import { documentApi } from "../services/document-api";
import { apiClient } from "../lib/api-client";

vi.mock("../lib/api-client");

describe("documentApi", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe("getDocumentPages", () => {
    it("ドキュメントページ一覧を取得する", async () => {
      const mockResponse = {
        page_count: 2,
        targets: [
          {
            id: "1",
            document_type: "トップページ",
            url: "https://example.com",
            description: null,
          },
        ],
      };

      vi.mocked(apiClient.get).mockResolvedValueOnce(mockResponse);

      const result = await documentApi.getDocumentPages();
      expect(result).toEqual(mockResponse);
      expect(apiClient.get).toHaveBeenCalledWith(
        "/api/v1/service-authorization/aws-iam/document-pages"
      );
    });
  });

  describe("getCrawlingTargets", () => {
    it("クローリング対象一覧を取得する", async () => {
      const mockResponse = {
        page_count: 1,
        targets: [
          {
            id: "1",
            site_id: "site-1",
            crawl_interval: 10,
            last_crawled_at: null,
            next_crawl_at: null,
            is_active: true,
            created_at: "2025-01-01T00:00:00Z",
            updated_at: "2025-01-01T00:00:00Z",
          },
        ],
      };

      vi.mocked(apiClient.get).mockResolvedValueOnce(mockResponse);

      const result = await documentApi.getCrawlingTargets();
      expect(result).toEqual(mockResponse);
      expect(apiClient.get).toHaveBeenCalledWith(
        "/api/v1/service-authorization/aws-iam/document-crawling-conditions"
      );
    });
  });

  describe("getCrawlingTarget", () => {
    it("特定のクローリング対象を取得する", async () => {
      const documentId = "doc-123";
      const mockResponse = {
        id: "1",
        site_id: documentId,
        crawl_interval: 10,
        last_crawled_at: null,
        next_crawl_at: null,
        is_active: true,
        created_at: "2025-01-01T00:00:00Z",
        updated_at: "2025-01-01T00:00:00Z",
      };

      vi.mocked(apiClient.get).mockResolvedValueOnce(mockResponse);

      const result = await documentApi.getCrawlingTarget(documentId);
      expect(result).toEqual(mockResponse);
      expect(apiClient.get).toHaveBeenCalledWith(
        `/api/v1/service-authorization/aws-iam/document-crawling-conditions/${documentId}`
      );
    });
  });

  describe("addCrawlingTarget", () => {
    it("クローリング対象を追加する", async () => {
      const documentId = "doc-123";
      const mockResponse = {
        id: "1",
        site_id: documentId,
        crawl_interval: 10,
        last_crawled_at: null,
        next_crawl_at: null,
        is_active: true,
        created_at: "2025-01-01T00:00:00Z",
        updated_at: "2025-01-01T00:00:00Z",
      };

      vi.mocked(apiClient.put).mockResolvedValueOnce(mockResponse);

      const result = await documentApi.addCrawlingTarget(documentId);
      expect(result).toEqual(mockResponse);
      expect(apiClient.put).toHaveBeenCalledWith(
        `/api/v1/service-authorization/aws-iam/document-crawling-conditions/${documentId}`
      );
    });
  });

  describe("deleteCrawlingTarget", () => {
    it("クローリング対象を削除する", async () => {
      const documentId = "doc-123";
      const mockResponse = { message: "Deleted the target." };

      vi.mocked(apiClient.delete).mockResolvedValueOnce(mockResponse);

      const result = await documentApi.deleteCrawlingTarget(documentId);
      expect(result).toEqual(mockResponse);
      expect(apiClient.delete).toHaveBeenCalledWith(
        `/api/v1/service-authorization/aws-iam/crawler-targets/${documentId}`
      );
    });
  });
});
