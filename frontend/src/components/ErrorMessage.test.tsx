/**
 * ErrorMessageコンポーネントのテスト
 */

import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { ErrorMessage } from "../components/ErrorMessage";

describe("ErrorMessage", () => {
  it("エラーメッセージが表示される", () => {
    const error = new Error("Test error message");
    render(<ErrorMessage error={error} />);

    expect(screen.getByText("エラーが発生しました")).toBeInTheDocument();
    expect(screen.getByText("Test error message")).toBeInTheDocument();
  });

  it("再試行ボタンが表示されクリックできる", () => {
    const error = new Error("Test error");
    const onRetry = vi.fn();

    render(<ErrorMessage error={error} onRetry={onRetry} />);

    const retryButton = screen.getByText("再試行");
    expect(retryButton).toBeInTheDocument();

    fireEvent.click(retryButton);
    expect(onRetry).toHaveBeenCalledTimes(1);
  });

  it("onRetryが指定されていない場合、再試行ボタンが表示されない", () => {
    const error = new Error("Test error");
    render(<ErrorMessage error={error} />);

    expect(screen.queryByText("再試行")).not.toBeInTheDocument();
  });
});
