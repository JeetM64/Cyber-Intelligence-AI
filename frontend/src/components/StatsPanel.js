import "./StatsPanel.css";

export default function StatsPanel({ data }) {
  return (
    <div className="stats-row">

      <div className="stat-card">
        <h4>Total Traffic</h4>
        <h2>{data.total_records}</h2>
      </div>

      <div className="stat-card alert">
        <h4>Threats Detected</h4>
        <h2>{data.anomalies_detected}</h2>
      </div>

      <div className="stat-card">
        <h4>Risk %</h4>
        <h2>{data.risk_percent}%</h2>
      </div>

      <div className="stat-card">
        <h4>Risk Level</h4>
        <h2>{data.risk_level}</h2>
      </div>

    </div>
  );
}
