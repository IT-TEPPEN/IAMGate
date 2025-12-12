/**
 * ホームページ
 */

import { Link } from "react-router";

export function HomePage() {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">IAM Gate</h1>
        <p className="text-xl text-gray-600 mb-8">
          AWS IAM権限管理アプリケーション
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Link
            to="/documents"
            className="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200"
          >
            <h2 className="text-2xl font-semibold text-gray-900 mb-2">
              ドキュメントページ
            </h2>
            <p className="text-gray-600">
              登録されているドキュメントページの一覧を確認できます
            </p>
          </Link>

          <Link
            to="/crawling-targets"
            className="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200"
          >
            <h2 className="text-2xl font-semibold text-gray-900 mb-2">
              クローリング対象管理
            </h2>
            <p className="text-gray-600">
              クローリング対象の追加・削除・確認ができます
            </p>
          </Link>
        </div>

        <div className="mt-12 p-6 bg-blue-50 rounded-lg">
          <h3 className="text-xl font-semibold text-gray-900 mb-3">主な機能</h3>
          <ul className="space-y-2 text-gray-700">
            <li className="flex items-start">
              <span className="mr-2">•</span>
              <span>
                IAM Action Catalog API:
                IAMドキュメントページのスクレイピングによる全IAMアクションのAPI提供
              </span>
            </li>
            <li className="flex items-start">
              <span className="mr-2">•</span>
              <span>管理者によるIAMアクションの許可管理</span>
            </li>
            <li className="flex items-start">
              <span className="mr-2">•</span>
              <span>ユーザーによるIAM権限リクエストのワークフロー</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}
