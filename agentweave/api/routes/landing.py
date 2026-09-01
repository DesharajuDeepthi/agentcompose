"""Web landing page — served at /."""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AgentWeave</title>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #0f1117;
    --card: #1a1d27;
    --border: #2a2d3a;
    --text: #e8eaf0;
    --muted: #6b7280;
    --accent: #6366f1;
    --accent-light: #818cf8;
    --green: #22c55e;
    --amber: #f59e0b;
  }
  body {
    background: var(--bg);
    color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 2rem;
  }
  .logo {
    font-size: 2.5rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.5rem;
  }
  .logo span { color: var(--accent-light); }
  .tagline {
    color: var(--muted);
    font-size: 1rem;
    margin-bottom: 2.5rem;
    text-align: center;
  }
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 1rem;
    width: 100%;
    max-width: 720px;
    margin-bottom: 2.5rem;
  }
  .card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1.25rem 1.5rem;
  }
  .card-label {
    font-size: 0.75rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.4rem;
  }
  .card-value {
    font-size: 1.1rem;
    font-weight: 600;
  }
  .dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 6px;
    background: var(--green);
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }
  .links {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    justify-content: center;
  }
  .links a {
    color: var(--accent-light);
    text-decoration: none;
    font-size: 0.9rem;
    border-bottom: 1px solid transparent;
    transition: border-color 0.15s;
  }
  .links a:hover { border-color: var(--accent-light); }
  .footer {
    margin-top: 3rem;
    color: var(--muted);
    font-size: 0.8rem;
    text-align: center;
  }
</style>
</head>
<body>
<div class="logo">Agent<span>Weave</span></div>
<p class="tagline">Config-driven multi-agent orchestration &mdash; LangGraph &middot; MCP &middot; A2A</p>

<div class="cards">
  <div class="card">
    <div class="card-label">Status</div>
    <div class="card-value"><span class="dot"></span>Running</div>
  </div>
  <div class="card">
    <div class="card-label">Version</div>
    <div class="card-value">0.1.0</div>
  </div>
  <div class="card">
    <div class="card-label">Default port</div>
    <div class="card-value">7777</div>
  </div>
</div>

<div class="links">
  <a href="/docs">API docs</a>
  <a href="/redoc">ReDoc</a>
  <a href="/health">Health</a>
  <a href="https://github.com/desharajudeepthi/agentweave" target="_blank">GitHub</a>
</div>

<p class="footer">AgentWeave &copy; 2026 Deepthi Desharaju &mdash; MIT License</p>
</body>
</html>"""


@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def landing() -> HTMLResponse:
    return HTMLResponse(content=_HTML)
