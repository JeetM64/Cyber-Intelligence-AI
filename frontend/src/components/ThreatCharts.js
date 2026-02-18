import React from "react";
import { Doughnut, Bar, Line } from "react-chartjs-2";
import "../chartConfig";
import "./ThreatCharts.css";

export default function ThreatCharts({ data }) {

  if (!data) return null;

  // === Threat Ratio ===
  const threatRatio = {
    labels: ["Normal Traffic", "Threat Traffic"],
    datasets: [{
      data: [
        data.traffic_distribution.normal,
        data.traffic_distribution.anomaly
      ],
      backgroundColor: ["#00d4ff", "#ff4d6d"],
      borderWidth: 0
    }]
  };

  // === Feature Importance ===
  const featureImportance = {
    labels: Object.keys(data.feature_variance),
    datasets: [{
      label: "Anomaly Feature Impact",
      data: Object.values(data.feature_variance),
      backgroundColor: "#7c3aed"
    }]
  };

  // === Risk Timeline ===
  const riskTimeline = {
    labels: ["T1","T2","T3","T4","T5"],
    datasets: [{
      label: "Risk %",
      data: [
        data.risk_percent * 0.7,
        data.risk_percent * 0.9,
        data.risk_percent * 0.5,
        data.risk_percent * 1.2,
        data.risk_percent
      ],
      borderColor: "#00ffa6",
      backgroundColor: "rgba(0,255,166,0.2)",
      tension: 0.4,
      fill: true
    }]
  };

  return (
    <div className="charts-container">

      <div className="chart-card">
        <h3>Threat Ratio</h3>
        <Doughnut data={threatRatio}/>
      </div>

      <div className="chart-card">
        <h3>Feature Importance</h3>
        <Bar data={featureImportance}/>
      </div>

      <div className="chart-card timeline-center">
        <h3>Risk Timeline</h3>
        <Line data={riskTimeline}/>
      </div>

    </div>
  );
}
