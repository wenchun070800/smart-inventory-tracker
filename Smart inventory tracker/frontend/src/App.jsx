// frontend/src/App.jsx
import React, { useEffect, useState } from 'react';

function App(){
  const [items, setItems] = useState([]);

  useEffect(()=>{
    fetch('/api/items').then(r=>r.json()).then(j=>setItems(j.items || []));
    const ws = new WebSocket(`${window.location.protocol === 'https:' ? 'wss' : 'ws'}://${window.location.host}/ws`);
    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);
      setItems(data.counts || []);
    };
    ws.onopen = () => console.log('ws open');
    ws.onclose = () => console.log('ws closed');
    return ()=> ws.close();
  },[]);

  return (
    <div style={{padding:20}}>
      <h2>Inventory Dashboard</h2>
      <table style={{borderCollapse:'collapse', width:'100%'}}>
        <thead>
          <tr><th style={{border:'1px solid #ccc', padding:8}}>SKU</th><th style={{border:'1px solid #ccc', padding:8}}>Name</th><th style={{border:'1px solid #ccc', padding:8}}>Count</th><th style={{border:'1px solid #ccc', padding:8}}>Last Seen</th><th style={{border:'1px solid #ccc', padding:8}}>Actions</th></tr>
        </thead>
        <tbody>
          {items.map(i=>(
            <tr key={i.sku}>
              <td style={{border:'1px solid #ccc', padding:8}}>{i.sku}</td>
              <td style={{border:'1px solid #ccc', padding:8}}>{i.name}</td>
              <td style={{border:'1px solid #ccc', padding:8}}>{i.count}</td>
              <td style={{border:'1px solid #ccc', padding:8}}>{i.last_seen ? new Date(i.last_seen).toLocaleString() : '-'}</td>
              <td style={{border:'1px solid #ccc', padding:8}}><button onClick={()=>alert('Reorder triggered for '+i.sku)}>Reorder</button></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;