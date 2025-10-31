import React, { useState } from "react";
import { forwardEmail } from "../api/api";

export default function ForwardEmail() {
  const [form, setForm] = useState({ parent_email: "", sender: "", receiver: "", body: "" });
  const [response, setResponse] = useState(null);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await forwardEmail(form);
    setResponse(res);
  };

  return (
    <div>
      <h2>Forward Email</h2>
      <form onSubmit={handleSubmit}>
        <input name="parent_email" placeholder="Parent Email ID" onChange={handleChange} required/><br />
        <input name="sender" placeholder="Sender" onChange={handleChange} required/><br />
        <input name="receiver" placeholder="Receiver" onChange={handleChange} required/><br />
        <textarea name="body" placeholder="Body" onChange={handleChange} required/><br />
        <button type="submit">Forward</button>
      </form>
      {response && (
        <div style={{ marginTop: "20px", padding: "10px", border: "1px solid #ccc", borderRadius: "5px" }}>
          {Object.entries(response).map(([key, value]) => (
            <div key={key}>
              <strong>{key}:</strong> {value.toString()}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}