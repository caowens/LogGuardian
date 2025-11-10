import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "LogGuardian",
  description: "Detect suspicious logs in real-time.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className="font-sans bg-gray-950 text-white"
      >
        {children}
      </body>
    </html>
  );
}
