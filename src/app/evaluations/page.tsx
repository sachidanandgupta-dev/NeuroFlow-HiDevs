export default function Evaluations() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Live Evaluation Feed</h1>
      <div className="space-y-4">
        {[1, 2, 3].map((i) => (
          <div key={i} className="border p-4 rounded flex justify-between items-center bg-white shadow-sm">
            <div>
              <p className="font-semibold">Query: "How does NeuroFlow work?"</p>
              <p className="text-sm text-gray-500">Pipeline: V2-Alpha • 2 mins ago</p>
            </div>
            <div className="flex gap-2">
              <span className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm">Faithfulness: 0.9</span>
              <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded-full text-sm">Score: 0.85</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}