import React from "react";

export default function Sidebar({ setView }) {
  return (
    <div style={{ width: "200px", borderRight: "1px solid #ccc", padding: "10px" }}>
      <h3>Menu</h3>
      <button onClick={() => setView("send")}>Send Email</button>
      <button onClick={() => setView("reply")}>Reply Email</button>
      <button onClick={() => setView("forward")}>Forward Email</button>
      <button onClick={() => setView("viewThread")}>View Thread</button>
      <button onClick={() => setView("viewEmails")}>View Emails</button>
      <button onClick={() => setView("viewClusters")}>View Clusters</button>
    </div>
  );
}

