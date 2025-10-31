const BASE_URL = "http://127.0.0.1:8000/emails"; // Base API URL

// ---------------- Email Actions ----------------
export async function sendEmail(data) {
  const res = await fetch(`${BASE_URL}/send/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function replyEmail(data) {
  const res = await fetch(`${BASE_URL}/reply/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

export async function forwardEmail(data) {
  const res = await fetch(`${BASE_URL}/forward/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  return res.json();
}

// ---------------- View Threads ----------------
export async function getAllThreads() {
  // Get list of all threads (root emails)
  const res = await fetch(`${BASE_URL}/threads/`);
  return res.json();
}

// Replaces old getEmailsInThread() → now uses root_email_id
export async function viewThread(root_email_id) {
  // Get all emails inside a specific thread
  const res = await fetch(`${BASE_URL}/thread/${root_email_id}/`);
  return res.json();
}

// ---------------- Other Endpoints ----------------
export async function viewAllEmails() {
  const res = await fetch(`${BASE_URL}/emails/`);
  return res.json();
}

export async function getClusters() {
  const res = await fetch(`${BASE_URL}/emailcluster/`);
  return res.json();
}




