import React from "react";

function ItemRow({ item }) {
  return (
    <tr>
      <td style={{ border: "1px solid #ccc", padding: 8 }}>{item.sku}</td>
      <td style={{ border: "1px solid #ccc", padding: 8 }}>{item.name}</td>
      <td style={{ border: "1px solid #ccc", padding: 8 }}>{item.count}</td>
      <td style={{ border: "1px solid #ccc", padding: 8 }}>
        {item.last_seen ? new Date(item.last_seen).toLocaleString() : "-"}
      </td>
      <td style={{ border: "1px solid #ccc", padding: 8 }}>
        <button onClick={() => alert(`Reorder triggered for ${item.sku}`)}>
          Reorder
        </button>
      </td>
    </tr>
  );
}

export default ItemRow;