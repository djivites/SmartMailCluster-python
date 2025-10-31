import React, { useState } from "react";
import { getClusters } from "../api/api";

export default function ViewClusters() {
  const [clusters, setClusters] = useState({});
  const [loading, setLoading] = useState(false);
  const [expanded, setExpanded] = useState({}); // Track which clusters are expanded
  const [clustersLoaded, setClustersLoaded] = useState(false); // Track if user attempted to load

  const handleClick = async () => {
    setLoading(true);
    try {
      const res = await getClusters(); // Call backend API
      setClusters(res.clusters || {}); // Default to empty object if no clusters
    } catch (error) {
      console.error("Error fetching clusters:", error);
      setClusters({});
    } finally {
      setLoading(false);
      setClustersLoaded(true); // Mark that clusters have been loaded
    }
  };

  const toggleCluster = (root) => {
    setExpanded(prev => ({ ...prev, [root]: !prev[root] }));
  };

  return (
    <div>
      <h2>View Clusters</h2>
      <button onClick={handleClick}>Load Clusters</button>

      {loading && <p>Loading...</p>}

      {!loading && clustersLoaded && Object.keys(clusters).length === 0 && (
        <p>No clusters available</p>
      )}

      {!loading && Object.keys(clusters).length > 0 && (
        <div>
          {Object.entries(clusters).map(([root, emails]) => (
            <div key={root} style={{ marginBottom: "15px", border: "1px solid #ccc", padding: "10px", borderRadius: "5px" }}>
              {/* Cluster header */}
              <div 
                style={{ cursor: "pointer", backgroundColor: "#f0f0f0", padding: "5px", borderRadius: "3px" }}
                onClick={() => toggleCluster(root)}
              >
                <strong>Cluster Root {root}</strong> (click to {expanded[root] ? "collapse" : "expand"})
              </div>

              {/* Emails in cluster */}
              {expanded[root] && (
                <div style={{ marginTop: "10px", paddingLeft: "15px" }}>
                  {emails.map((email) => (
                    <div key={email.email_id} style={{ marginBottom: "10px", borderBottom: "1px dashed #aaa", paddingBottom: "5px" }}>
                      <p><strong>From:</strong> {email.sender} | <strong>To:</strong> {email.receiver}</p>
                      <p><strong>Subject:</strong> {email.subject}</p>
                      <p><strong>Body:</strong> {email.body}</p>
                    </div>
                  ))}
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
