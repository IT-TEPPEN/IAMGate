/**
 * Loadingコンポーネントのテスト
 */

import { describe, it, expect } from "vitest";
import { render } from "@testing-library/react";
import { Loading } from "../components/Loading";

describe("Loading", () => {
  it("ローディングインジケーターが表示される", () => {
    const { container } = render(<Loading />);
    const loadingElement = container.querySelector(".animate-spin");
    expect(loadingElement).toBeInTheDocument();
  });
});
