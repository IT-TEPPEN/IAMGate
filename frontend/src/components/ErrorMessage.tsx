/**
 * 共通コンポーネント: ErrorMessage
 */

interface ErrorMessageProps {
  error: Error;
  onRetry?: () => void;
}

export function ErrorMessage({ error, onRetry }: ErrorMessageProps) {
  return (
    <div className="bg-red-50 border border-red-200 rounded-lg p-4 my-4">
      <h3 className="text-red-800 font-semibold mb-2">エラーが発生しました</h3>
      <p className="text-red-700 mb-4">{error.message}</p>
      {onRetry && (
        <button
          onClick={onRetry}
          className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700 transition-colors"
        >
          再試行
        </button>
      )}
    </div>
  );
}
