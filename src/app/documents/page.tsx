export default function Documents() {
  return (
    <div className="p-8">
      <h1 className="text-2xl font-bold mb-4">Documents</h1>
      <div className="border-2 border-dashed border-gray-300 p-12 text-center rounded-lg bg-gray-50 mb-8">
        <p className="text-gray-600">Drag and drop files here to upload</p>
        <button className="mt-2 text-blue-600 underline">Browse files</button>
      </div>

      <table className="w-full text-left">
        <thead>
          <tr className="border-b">
            <th className="py-2">Filename</th>
            <th>Status</th>
            <th>Chunks</th>
          </tr>
        </thead>
        <tbody>
          <tr className="border-b">
            <td className="py-2">System_Architecture.pdf</td>
            <td><span className="text-blue-500 animate-pulse">● processing</span></td>
            <td>124</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}