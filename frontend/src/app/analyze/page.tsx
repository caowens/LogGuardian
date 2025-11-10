import FileUploader from "@/components/FileUploader";

export default function AnalyzePage() {
  return (
    <main className="min-h-screen bg-gray-950 text-white p-8">
      <h1 className="text-2xl font-bold mb-6 text-center">Analyze Logs</h1>
      <FileUploader />
    </main>
  );
}