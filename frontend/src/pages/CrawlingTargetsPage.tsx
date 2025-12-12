/**
 * クローリング対象管理画面
 */

import { useState } from "react";
import { documentApi } from "../services/document-api";
import { useApi } from "../hooks/useApi";
import { Loading } from "../components/Loading";
import { ErrorMessage } from "../components/ErrorMessage";

export function CrawlingTargetsPage() {
  const { data, loading, error, refetch } = useApi(() =>
    documentApi.getCrawlingTargets()
  );
  const [selectedDocumentId, setSelectedDocumentId] = useState<string>("");
  const [actionLoading, setActionLoading] = useState(false);
  const [actionError, setActionError] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleAddTarget = async (documentId: string) => {
    if (!documentId.trim()) {
      setActionError("ドキュメントIDを入力してください");
      return;
    }

    try {
      setActionLoading(true);
      setActionError(null);
      setSuccessMessage(null);
      await documentApi.addCrawlingTarget(documentId);
      setSuccessMessage("クローリング対象を追加しました");
      setSelectedDocumentId("");
      await refetch();
    } catch (err) {
      setActionError(err instanceof Error ? err.message : "追加に失敗しました");
    } finally {
      setActionLoading(false);
    }
  };

  const handleDeleteTarget = async (documentId: string) => {
    if (!confirm("本当に削除しますか？")) {
      return;
    }

    try {
      setActionLoading(true);
      setActionError(null);
      setSuccessMessage(null);
      await documentApi.deleteCrawlingTarget(documentId);
      setSuccessMessage("クローリング対象を削除しました");
      await refetch();
    } catch (err) {
      setActionError(err instanceof Error ? err.message : "削除に失敗しました");
    } finally {
      setActionLoading(false);
    }
  };

  if (loading) {
    return <Loading />;
  }

  if (error) {
    return <ErrorMessage error={error} onRetry={refetch} />;
  }

  if (!data) {
    return <div>データがありません</div>;
  }

  return (
    <div className="container mx-auto px-4 py-8">
      <div className="mb-6">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">
          クローリング対象管理
        </h1>
        <p className="text-gray-600">
          全{data.page_count}件のクローリング対象が登録されています
        </p>
      </div>

      {/* 追加フォーム */}
      <div className="bg-white rounded-lg shadow p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">新規追加</h2>
        <div className="flex gap-4">
          <input
            type="text"
            value={selectedDocumentId}
            onChange={(e) => setSelectedDocumentId(e.target.value)}
            placeholder="ドキュメントID"
            className="flex-1 px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
            disabled={actionLoading}
          />
          <button
            onClick={() => handleAddTarget(selectedDocumentId)}
            disabled={actionLoading}
            className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 transition-colors disabled:bg-gray-400"
          >
            {actionLoading ? "処理中..." : "追加"}
          </button>
        </div>
      </div>

      {/* メッセージ表示 */}
      {actionError && (
        <div className="bg-red-50 border border-red-200 rounded-lg p-4 mb-4">
          <p className="text-red-700">{actionError}</p>
        </div>
      )}

      {successMessage && (
        <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
          <p className="text-green-700">{successMessage}</p>
        </div>
      )}

      {/* クローリング対象一覧 */}
      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                ID
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                サイトID
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                間隔(分)
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                最終実行
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                次回実行
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                状態
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                操作
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {data.targets.map((target) => (
              <tr key={target.site_property_id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  -
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {target.site_property_id}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {target.crawl_interval_minutes}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  -
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                  -
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span
                    className={`px-2 inline-flex text-xs leading-5 font-semibold rounded-full ${
                      target.is_active
                        ? "bg-green-100 text-green-800"
                        : "bg-gray-100 text-gray-800"
                    }`}
                  >
                    {target.is_active ? "有効" : "無効"}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm">
                  <button
                    onClick={() => handleDeleteTarget(target.site_id)}
                    disabled={actionLoading}
                    className="text-red-600 hover:text-red-900 disabled:text-gray-400"
                  >
                    削除
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-4">
        <button
          onClick={refetch}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition-colors"
        >
          再読み込み
        </button>
      </div>
    </div>
  );
}
