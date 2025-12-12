/**
 * ドキュメントページ一覧画面
 */

import { documentApi } from "../services/document-api";
import { useApi } from "../hooks/useApi";
import { Loading } from "../components/Loading";
import { ErrorMessage } from "../components/ErrorMessage";

export function DocumentPagesPage() {
  const { data, loading, error, refetch } = useApi(() =>
    documentApi.getDocumentPages()
  );

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
          ドキュメントページ一覧
        </h1>
        <p className="text-gray-600">
          全{data.page_count}件のドキュメントページが登録されています
        </p>
      </div>

      <div className="bg-white rounded-lg shadow overflow-hidden">
        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                ID
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                タイプ
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                URL
              </th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                説明
              </th>
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {data.targets.map((page) => (
              <tr key={page.id} className="hover:bg-gray-50">
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {page.id}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-900">
                  {page.document_type}
                </td>
                <td className="px-6 py-4 text-sm text-blue-600 hover:text-blue-800">
                  <a
                    href={page.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="underline"
                  >
                    {page.url}
                  </a>
                </td>
                <td className="px-6 py-4 text-sm text-gray-500">
                  {page.description || "-"}
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
