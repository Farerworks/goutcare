export default async function Home() {
  const api = process.env.NEXT_PUBLIC_API_BASE_URL || "http://backend:8000";
  let status = "unknown";
  try {
    const res = await fetch(`${api}/api/v1/health`, { cache: "no-store" });
    const json = await res.json();
    status = json.status || "ok";
  } catch (e) {
    status = "api not reachable";
  }

  return (
    <main style={{ padding: 24 }}>
      <h1>GoutCare (MVP Skeleton)</h1>
      <p>API health: <b>{status}</b></p>
    </main>
  );
}