export async function fetchItems() {
  const res = await fetch("/api/items");
  return res.json();
}

export async function sendDetection(payload) {
  const res = await fetch("/api/detections", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  return res.json();
}