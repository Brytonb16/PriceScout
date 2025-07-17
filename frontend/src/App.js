
import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [inStockOnly, setInStockOnly] = useState(false);

  const searchParts = async () => {
    setLoading(true);
    try {
      const response = await fetch(`https://pricescout-8xg5.onrender.com/api/search?q=${encodeURIComponent(query)}&inStock=${inStockOnly}`);
      const data = await response.json();
      setResults(data);
    } catch (err) {
      console.error(err);
      setResults([]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>PriceScout</h1>
      <div className="search-bar">
        <input value={query} onChange={e => setQuery(e.target.value)} placeholder="Enter part name or model #" />
        <label><input type="checkbox" checked={inStockOnly} onChange={() => setInStockOnly(!inStockOnly)} /> In Stock Only</label>
        <button onClick={searchParts}>Search</button>
      </div>
      {loading && <p>Loading...</p>}
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Price</th>
            <th>Source</th>
            <th>In Stock</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          {results.map((item, index) => (
            <tr key={index}>
              <td>{item.title}</td>
              <td>${item.price.toFixed(2)}</td>
              <td>{item.source}</td>
              <td>{item.in_stock ? "Yes" : "No"}</td>
              <td><a href={item.link} target="_blank" rel="noreferrer">View</a></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;
