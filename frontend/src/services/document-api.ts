/**
 * Document API Service
 * ドキュメントサイトとクローリング対象の管理に関するAPI呼び出し
 */

import { apiClient } from "../lib/api-client";
import type {
  DocumentPagesResponse,
  CrawlingTargetsResponse,
  DocumentSiteCrawlingCondition,
  DeleteTargetResponse,
} from "../types/api";

const BASE_PATH = "/api/v1/service-authorization/aws-iam";

export const documentApi = {
  /**
   * ドキュメントページ一覧を取得
   */
  async getDocumentPages(): Promise<DocumentPagesResponse> {
    return apiClient.get<DocumentPagesResponse>(`${BASE_PATH}/document-pages`);
  },

  /**
   * クローリング対象一覧を取得
   */
  async getCrawlingTargets(): Promise<CrawlingTargetsResponse> {
    return apiClient.get<CrawlingTargetsResponse>(
      `${BASE_PATH}/document-crawling-conditions`
    );
  },

  /**
   * 特定のクローリング対象を取得
   */
  async getCrawlingTarget(
    documentId: string
  ): Promise<DocumentSiteCrawlingCondition> {
    return apiClient.get<DocumentSiteCrawlingCondition>(
      `${BASE_PATH}/document-crawling-conditions/${documentId}`
    );
  },

  /**
   * クローリング対象を追加・更新
   */
  async addCrawlingTarget(
    documentId: string
  ): Promise<DocumentSiteCrawlingCondition> {
    return apiClient.put<DocumentSiteCrawlingCondition>(
      `${BASE_PATH}/document-crawling-conditions/${documentId}`
    );
  },

  /**
   * クローリング対象を削除
   */
  async deleteCrawlingTarget(
    documentId: string
  ): Promise<DeleteTargetResponse> {
    return apiClient.delete<DeleteTargetResponse>(
      `${BASE_PATH}/crawler-targets/${documentId}`
    );
  },
};
