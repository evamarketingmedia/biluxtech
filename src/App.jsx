import React from "react";
import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home.jsx";
import ServicePage from "./pages/ServicePage.jsx";

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/servizi/:slug" element={<ServicePage />} />
    </Routes>
  );
}
