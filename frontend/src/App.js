import React, { useState } from "react";
import "./App.css";

import UploadZone from "./components/UploadZone";
import StatsPanel from "./components/StatsPanel";
import ThreatCharts from "./components/ThreatCharts";
import Insights from "./components/Insights";

export default function App() {
  const [analysis, setAnalysis] = useState(null);

  const uploadFile = async (file) => {
    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch("http://127.0.0.1:8000/upload", {
        method: "POST",
        body: formData
      });

      const data = await res.json();
      setAnalysis(data);

    } catch (err) {
      alert("Backend not running or error uploading file");
      console.error(err);
    }
  };

  return (
    <div className="app">

      {/* HEADER */}
      <header className="header">
        <h1>Cyber Intelligence AI</h1>
        <p>AI-Driven Network Threat Detection Dashboard</p>
      </header>

      {/* FILE UPLOAD */}
      <UploadZone onUpload={uploadFile} />

      {/* DASHBOARD */}
      {analysis && (
        <>
          <StatsPanel data={analysis} />
          <ThreatCharts data={analysis} />
          <Insights data={analysis} />
        </>
      )}

    </div>
  );
}
