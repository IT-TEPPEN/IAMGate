/**
 * Appコンポーネント
 * ルーティング設定
 */

import { BrowserRouter, Routes, Route } from "react-router";
import { Layout } from "./components/Layout";
import { HomePage } from "./pages/HomePage";
import { DocumentPagesPage } from "./pages/DocumentPagesPage";
import { CrawlingTargetsPage } from "./pages/CrawlingTargetsPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="documents" element={<DocumentPagesPage />} />
          <Route path="crawling-targets" element={<CrawlingTargetsPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
