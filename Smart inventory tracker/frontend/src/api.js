export async function fetchItems() {
  const res = await fetch('/api/items');
  return res.json();
}