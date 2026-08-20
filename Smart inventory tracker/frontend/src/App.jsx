import React, { useEffect, useState } from 'react';
import Dashboard from "./components/Dashboard";
import Charts from "./components/Charts";

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
      <Dashboard items={items} />
      <Charts items={items} />
    </div>
  );
}

export default App;
