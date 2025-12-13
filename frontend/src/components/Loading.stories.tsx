/**
 * Storybook: Loading Component
 */

import type { Meta, StoryObj } from "@storybook/react-vite";
import { Loading } from "./Loading";

const meta = {
  title: "Components/Loading",
  component: Loading,
  parameters: {
    layout: "centered",
  },
  tags: ["autodocs"],
} satisfies Meta<typeof Loading>;

export default meta;
type Story = StoryObj<typeof meta>;

/**
 * デフォルトの Loading コンポーネント
 */
export const Default: Story = {};

/**
 * フルスクリーン表示の Loading コンポーネント
 */
export const FullScreen: Story = {
  parameters: {
    layout: "fullscreen",
  },
};
