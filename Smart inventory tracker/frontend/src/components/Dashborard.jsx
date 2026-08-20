import React from "react";

function Dashboard({ items }) {
  return (
    <table style={{ borderCollapse: "collapse", width: "100%" }}>
      <thead>
        <tr>
          <th style={{ border: "1px solid #ccc", padding: 8 }}>SKU</th>
          <th style={{ border: "1px solid #ccc", padding: 8 }}>Name</th>
          <th style={{ border: "1px solid #ccc", padding: 8 }}>Count</th>
          <th style={{ border: "1px solid #ccc", padding: 8 }}>Last Seen</th>
          <th style={{ border: "1px solid #ccc", padding: 8 }}>Actions</th>
        </tr>
      </thead>
      <tbody>
        {items.map((i) => (
          <tr key={i.sku}>
            <td style={{ border: "1px solid #ccc", padding: 8 }}>{i.sku}</td>
            <td style={{ border: "1px solid #ccc", padding: 8 }}>{i.name}</td>
            <td style={{ border: "1px solid #ccc", padding: 8 }}>{i.count}</td>
            <td style={{ border: "1px solid #ccc", padding: 8 }}>
              {i.last_seen ? new Date(i.last_seen).toLocaleString() : "-"}
            </td>
            <td style={{ border: "1px solid #ccc", padding: 8 }}>
              <button onClick={() => alert(`Reorder triggered for ${i.sku}`)}>
                Reorder
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default Dashboard;