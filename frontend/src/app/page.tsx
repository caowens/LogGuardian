import Link from "next/link";

export default function Home() {
  return (
    <main className="flex flex-col items-center justify-center h-screen text-center space-y-6">
      <h1 className="text-4xl font-bold">🧠 LogGuardian</h1>
      <p className="text-gray-600 max-w-xl">
        Scan logs, detect suspicious patterns, and visualize security threats in real time.
      </p>
      <div className="space-x-4">
        <Link href="/demo" className="bg-blue-600 text-white px-4 py-2 rounded">Live Demo</Link>
        <Link href="/analyze" className="bg-gray-700 text-white px-4 py-2 rounded">Try Analyzer</Link>
      </div>
    </main>
  );
}
