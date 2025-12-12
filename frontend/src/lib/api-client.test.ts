/**
 * APIクライアントのテスト
 */

import { describe, it, expect, beforeEach, vi } from "vitest";
import { apiClient, ApiError } from "../lib/api-client";

// fetchのモック
global.fetch = vi.fn();

describe("apiClient", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe("get", () => {
    it("正常なレスポンスを返す", async () => {
      const mockData = { message: "success" };
      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockData,
      });

      const result = await apiClient.get("/test");
      expect(result).toEqual(mockData);
      expect(global.fetch).toHaveBeenCalledWith(
        "http://localhost:8000/test",
        expect.objectContaining({
          method: "GET",
        })
      );
    });

    it("エラーレスポンスでApiErrorをスローする", async () => {
      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: false,
        status: 404,
        json: async () => ({ detail: "Not found" }),
      });

      await expect(apiClient.get("/test")).rejects.toThrow(ApiError);
    });
  });

  describe("post", () => {
    it("データを送信して正常なレスポンスを返す", async () => {
      const mockData = { id: 1 };
      const postData = { name: "test" };

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockData,
      });

      const result = await apiClient.post("/test", postData);
      expect(result).toEqual(mockData);
      expect(global.fetch).toHaveBeenCalledWith(
        "http://localhost:8000/test",
        expect.objectContaining({
          method: "POST",
          body: JSON.stringify(postData),
        })
      );
    });
  });

  describe("put", () => {
    it("データを送信して正常なレスポンスを返す", async () => {
      const mockData = { id: 1, updated: true };
      const putData = { name: "updated" };

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockData,
      });

      const result = await apiClient.put("/test/1", putData);
      expect(result).toEqual(mockData);
      expect(global.fetch).toHaveBeenCalledWith(
        "http://localhost:8000/test/1",
        expect.objectContaining({
          method: "PUT",
          body: JSON.stringify(putData),
        })
      );
    });
  });

  describe("delete", () => {
    it("削除リクエストを送信して正常なレスポンスを返す", async () => {
      const mockData = { message: "deleted" };

      (global.fetch as ReturnType<typeof vi.fn>).mockResolvedValueOnce({
        ok: true,
        json: async () => mockData,
      });

      const result = await apiClient.delete("/test/1");
      expect(result).toEqual(mockData);
      expect(global.fetch).toHaveBeenCalledWith(
        "http://localhost:8000/test/1",
        expect.objectContaining({
          method: "DELETE",
        })
      );
    });
  });
});
