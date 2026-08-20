import React from "react";

function Charts({ items }) {
  return (
    <div style={{ marginTop: 20 }}>
      <h3>Charts Placeholder</h3>
      <p>Integrate Chart.js or Recharts here.</p>
      <ul>
        {items.map((i) => (
          <li key={i.sku}>
            {i.sku}: last count {i.count}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Charts;