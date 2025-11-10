import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen bg-gray-950 text-white">
      <h1 className="text-4xl font-bold mb-4">🛡️ LogGuardian</h1>
      <p className="text-gray-400 mb-8">
        Scan logs, detect suspicious patterns, and visualize security threats in real time.
      </p>

      <div className="space-x-4">
        <Link
          href="/analyze"
          className="bg-blue-600 px-4 py-2 rounded-md hover:bg-blue-700"
        >
          Upload Logs
        </Link>
        <Link
          href="/live"
          className="bg-green-600 px-4 py-2 rounded-md hover:bg-green-700"
        >
          View Live Demo
        </Link>
      </div>
    </main>
  );
}
