import React, { useState } from 'react';
import axios from 'axios';

export default function Dashboard() {
  const [sqlType, setSqlType] = useState('mysql');
  const [query, setQuery] = useState('SELECT * FROM users LIMIT 10;');
  const [mongoFilter, setMongoFilter] = useState('{}');
  const [collection, setCollection] = useState('products');
  const [result, setResult] = useState(null);

  const runSql = async () => {
    const res = await axios.post('http://localhost:8000/sql/query', {
      db_type: sqlType,
      query: query,
    });
    setResult(res.data);
  };

  const runMongo = async () => {
    const res = await axios.post('http://localhost:8000/mongo/query', {
      collection: collection,
      filter: JSON.parse(mongoFilter),
    });
    setResult(res.data);
  };

  return (
    <div className="p-4 max-w-4xl mx-auto">
      <h1 className="text-xl font-bold mb-4">Universal Data Manager – Dashboard</h1>

      <div className="mb-4">
        <h2 className="font-semibold">SQL Query</h2>
        <select value={sqlType} onChange={e => setSqlType(e.target.value)} className="border p-1">
          <option value="mysql">MySQL</option>
          <option value="postgres">PostgreSQL</option>
        </select>
        <textarea className="w-full border p-2 mt-2" rows={4} value={query} onChange={e => setQuery(e.target.value)} />
        <button onClick={runSql} className="bg-blue-600 text-white px-4 py-2 mt-2">Run SQL</button>
      </div>

      <div className="mb-4">
        <h2 className="font-semibold">MongoDB Query</h2>
        <input className="border p-1 mr-2" value={collection} onChange={e => setCollection(e.target.value)} placeholder="Collection" />
        <textarea className="w-full border p-2 mt-2" rows={4} value={mongoFilter} onChange={e => setMongoFilter(e.target.value)} />
        <button onClick={runMongo} className="bg-green-600 text-white px-4 py-2 mt-2">Run Mongo</button>
      </div>

      <div className="mt-4">
        <h2 className="font-semibold">Ergebnisse</h2>
        <pre className="bg-gray-100 p-2 mt-2 max-h-96 overflow-auto">{JSON.stringify(result, null, 2)}</pre>
      </div>
    </div>
  );
}
