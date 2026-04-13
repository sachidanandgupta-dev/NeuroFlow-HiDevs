"use client";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const data = [
  { name: 'P50', val: 400 },
  { name: 'P95', val: 700 },
  { name: 'P99', val: 1200 },
];

export default function Pipelines() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-6">Pipeline Manager</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="border p-4 rounded shadow">
          <h2 className="font-bold">Production RAG Pipeline</h2>
          <p className="text-green-600 font-medium">Status: Healthy (Score: 0.92)</p>
          <div className="h-40 w-full mt-4">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={data}><Bar dataKey="val" fill="#2563eb" /></BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}