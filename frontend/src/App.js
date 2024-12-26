import React, { useState } from 'react';

function App() {
  const [data, setData] = useState([]);

  const fetchData = async () => {
    const response = await fetch('/api/scrape');
    const result = await response.json();
    setData(result.titles);
  };

  return (
    <div>
      <h1>Agente de IA - Coletor de Dados</h1>
      <button onClick={fetchData}>Coletar Dados</button>
      <ul>
        {data.map((title, index) => (
          <li key={index}>{title}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
