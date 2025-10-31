import React, { useState } from "react";
import { sendEmail } from "../api/api";

export default function SendEmail() {
  const [form, setForm] = useState({ sender: "", receiver: "", subject: "", body: "" });
  const [response, setResponse] = useState(null);

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await sendEmail(form);
    setResponse(res);
  };

  return (
    <div>
      <h2>Send Email</h2>
      <form onSubmit={handleSubmit}>
        <input name="sender" placeholder="Sender" onChange={handleChange} required/><br />
        <input name="receiver" placeholder="Receiver" onChange={handleChange} required/><br />
        <input name="subject" placeholder="Subject" onChange={handleChange} required/><br />
        <textarea name="body" placeholder="Body" onChange={handleChange} required/><br />
        <button type="submit">Send</button>
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
    
