import React, { useState } from "react";

// Import the new API function
import { viewAllEmails } from "../api/api";

export default function ViewEmails() {
  const [emails, setEmails] = useState(null);

  const handleClick = async () => {
    try {
      const res = await viewAllEmails(); // call the new endpoint
      setEmails(res.emails); // set emails array
    } catch (err) {
      console.error("Error fetching emails:", err);
    }
  };

  return (
    <div>
      <h2>View All Emails</h2>
      <button onClick={handleClick}>Load Emails</button>

      {emails && emails.length > 0 ? (
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              <th>ID</th>
              <th>From</th>
              <th>To</th>
              <th>Subject</th>
              <th>Body</th>
              <th>Parent Email</th>
              <th>Thread_id</th>
            </tr>
          </thead>
          <tbody>
            {emails.map((email) => (
              <tr key={email.email_id}>
                <td>{email.email_id}</td>
                <td>{email.sender}</td>
                <td>{email.receiver}</td>
                <td>{email.subject}</td>
                <td>{email.body}</td>
                <td>{email.parent_email_id || "-"}</td>
                <td>{email.thread_id}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        emails && <p>No emails found.</p>
      )}
    </div>
  );
}

