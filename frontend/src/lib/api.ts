// src/lib/api.ts

export const BACKEND_URL =
  process.env.NEXT_PUBLIC_API_URL || "http://127.0.0.1:8000";

export interface Alert {
  detector: string;
  severity: "low" | "medium" | "high";
  confidence: number;
  message: string;
  log: string;
  meta: Record<string, any>;
}

export interface AlertReport {
  alerts: Alert[];
  count: number;
}

export async function analyzeLogs(file: File): Promise<AlertReport> {
  const formData = new FormData();
  formData.append("upload", file);

  const res = await fetch(`${BACKEND_URL}/api/analyze/scan`, {
    method: "POST",
    body: formData,
  });

  if (!res.ok) {
    throw new Error(`Failed to analyze logs: status code: ${res.status}`);
  }

  return res.json();
}
