"use client";

import { useState } from "react";
import { analyzeLogs, AlertReport } from "@/lib/api";

export default function FileUploader() {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState<AlertReport | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    try {
      const data = await analyzeLogs(file);
      setResult(data);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="p-6 border rounded-xl bg-gray-900 text-white max-w-xl mx-auto">
      <h2 className="text-lg font-semibold mb-3">Upload Logs for Analysis</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".txt"
          onChange={(e) => setFile(e.target.files?.[0] || null)}
          className="mb-3 file:cursor-pointer file:bg-gray-700 file:text-white file:px-3 file:py-1 file:rounded-md"
        />
        <button
          type="submit"
          disabled={!file || loading}
          className="bg-blue-600 px-4 py-2 rounded-md hover:bg-blue-700"
        >
          {loading ? "Analyzing..." : "Scan Logs"}
        </button>
      </form>

      {result && (
        <div className="mt-4">
          <h3 className="text-md font-semibold mb-2">
            {result.count} Alerts Detected
          </h3>
          <pre className="bg-gray-800 p-3 rounded-md text-sm overflow-x-auto">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
