import "./Insights.css";

export default function Insights({ data }) {
  return (
    <div className="insight-box">
      <h2>AI Threat Intelligence</h2>

      <p>
        Detected <b>{data.anomalies_detected}</b> anomalies out of{" "}
        <b>{data.total_records}</b> records.
      </p>

      <p>
        Current risk level is <b>{data.risk_level}</b>
        {" "}({data.risk_percent}% anomaly probability).
      </p>

      <p>
        High variance features indicate unusual protocol activity.
        Recommended action: firewall inspection and IDS log monitoring.
      </p>
    </div>
  );
}
