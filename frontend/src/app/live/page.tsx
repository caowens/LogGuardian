import LiveChart from "@/components/LiveChart";

export default function LivePage() {
  return (
    <main className="min-h-screen bg-gray-950 text-white p-8">
      <h1 className="text-2xl font-bold mb-6 text-center">Live Demo</h1>
      <LiveChart />
    </main>
  );
}
