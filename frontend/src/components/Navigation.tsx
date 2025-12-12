/**
 * ナビゲーションコンポーネント
 */

import { Link } from "react-router";

export function Navigation() {
  return (
    <nav className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="text-xl font-bold text-gray-900">
            IAM Gate
          </Link>

          <div className="flex space-x-4">
            <Link
              to="/documents"
              className="text-gray-700 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-100 transition-colors"
            >
              ドキュメント
            </Link>
            <Link
              to="/crawling-targets"
              className="text-gray-700 hover:text-gray-900 px-3 py-2 rounded-md text-sm font-medium hover:bg-gray-100 transition-colors"
            >
              クローリング対象
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
}
