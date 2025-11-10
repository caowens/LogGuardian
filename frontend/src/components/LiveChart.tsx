"use client";

import { useEffect, useState } from "react";
import { BACKEND_URL } from "@/lib/api";

interface LiveEvent {
    type: string;
    timestamp: number;
    severity: string;
    log: string;
}

export default function LiveChart() {
  const [events, setEvents] = useState<LiveEvent[]>([]);

  useEffect(() => {
    const eventSource = new EventSource(`${BACKEND_URL}/api/live/stream`);

    eventSource.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setEvents((prev) => [...prev.slice(-49), data]);
    };

    eventSource.onerror = () => {
      console.error("SSE connection error");
      eventSource.close();
    };

    return () => eventSource.close();
  }, []);

  return (
    <div className="p-6 bg-gray-900 text-white rounded-xl max-w-xl mx-auto">
      <h2 className="text-lg font-semibold mb-3">Live Log Stream</h2>
      <div className="overflow-y-auto max-h-80 space-y-2">
        {events.map((e, i) => (
          <div key={i} className="p-2 border-b border-gray-700">
            <strong>{e.severity.toUpperCase()}</strong> — {e.log}
          </div>
        ))}
      </div>
    </div>
  );
}
