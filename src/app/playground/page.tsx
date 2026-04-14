"use client";
import { useState } from 'react';

export default function Playground() {
  const [query, setQuery] = useState("");
  const [compareMode, setCompareMode] = useState(false);

  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Query Playground</h1>
      <div className="flex gap-4 mb-4">
        <select className="border p-2 rounded w-64 bg-white text-black">
          <option>Select Pipeline (Avg Score: 0.85)</option>
        </select>
        {compareMode && (
          <select className="border p-2 rounded w-64 bg-white text-black">
            <option>Select Second Pipeline</option>
          </select>
        )}
      </div>

      <div className="mb-4">
        <textarea 
          className="w-full border p-4 h-32 rounded bg-gray-50 text-black" 
          placeholder="Enter your query..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <p className="text-sm text-gray-500">{query.length} characters</p>
      </div>

      <button 
        onClick={() => setCompareMode(!compareMode)}
        className="bg-blue-600 text-white px-4 py-2 rounded"
      >
        {compareMode ? "Disable Compare" : "Enable Compare Mode"}
      </button>

      <div className="mt-8 border-t pt-4">
        <h3 className="font-semibold">Response Panel</h3>
        <div className="bg-gray-100 p-4 mt-2 rounded min-h-[100px] animate-pulse">
          Waiting for stream...
        </div>
      </div>
    </div>
  );
}