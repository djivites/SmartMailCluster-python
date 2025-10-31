import React, { useState, useEffect } from "react";
import { getAllThreads, viewThread } from "../api/api";

export default function ViewThread() {
  const [threads, setThreads] = useState([]);
  const [selectedEmails, setSelectedEmails] = useState(null);
  const [selectedThreadId, setSelectedThreadId] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch all threads when component mounts
  useEffect(() => {
    const fetchThreads = async () => {
      try {
        const res = await getAllThreads();
        setThreads(res.threads || []);
      } catch (error) {
        console.error("Error fetching threads:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchThreads();
  }, []);

  const handleThreadClick = async (root_email_id) => {
    setSelectedThreadId(root_email_id);
    try {
      const res = await viewThread(root_email_id);
      setSelectedEmails(res.emails || []);
    } catch (error) {
      console.error("Error fetching emails:", error);
      setSelectedEmails([]);
    }
  };

  return (
    <div>
      <h2>View Threads</h2>

      {loading ? (
        <p>Loading threads...</p>
      ) : threads.length === 0 ? (
        <p>No threads found.</p>
      ) : (
        <ul>
          {threads.map((thread) => (
            <li key={thread.thread_id}>
              <button onClick={() => handleThreadClick(thread.root_email.email_id)}>
                {thread.root_email.subject} (Root Email ID: {thread.root_email.email_id})
              </button>
            </li>
          ))}
        </ul>
      )}

      {selectedEmails && (
        <div>
          <h3>Emails in Thread {selectedThreadId}</h3>
          {selectedEmails.length === 0 ? (
            <p>No emails found in this thread.</p>
          ) : (
            <ul>
              {selectedEmails.map((email) => (
                <li key={email.email_id}>
                  {/* 🔄 Check both keys: sender/from, receiver/to */}
                  <strong>From:</strong> {email.sender || email.from} | <strong>To:</strong> {email.receiver || email.to} <br />
                  <strong>Subject:</strong> {email.subject} <br />
                  <strong>Body:</strong> {email.body} <br />
                  {/* 🔄 Parent Email ID */}
                  <strong>Parent Email ID:</strong> {email.parent_email_id || email.parent_email || "None"}
                  <hr />
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  );
}



