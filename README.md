# Module 5 — Consume the team-tickets MCP from Python

Kimi K2 doesn't natively speak MCP — but you have a pre-built MCP server (`tusharbisht/aie-team-tickets-mcp`, written in Node) that exposes your team's ticket data. Bridge the gap with a Python adapter.

## Setup
```bash
# Clone + run the MCP server
cd /tmp
git clone https://github.com/tusharbisht/aie-team-tickets-mcp
cd aie-team-tickets-mcp
npm install
# leave it; harness/mcp_adapter.py spawns it as a subprocess

# Back in the course repo
cd /tmp/kimi-assets/kimi-eng-course-repo
```

## Two exercises

1. **Implement `harness/mcp_adapter.py`** (~25 min)
   Rename `mcp_adapter.py-STUB` → `mcp_adapter.py` and fill the TODOs. Real JSON-RPC: spawn the server, `initialize`, `tools/list`, translate MCP shape to OpenAI tool_call shape, expose `call_tool(name, args)`.

2. **Use it from your M4 harness loop** (~15 min)
   Modify `harness/loop.py` to also include the MCP-bridged tools. Ask Kimi: "Find recent tickets tagged `payments-api` and tell me which one I should pick up next." Watch Kimi call `list_recent_tickets` via your adapter.

## MCP JSON-RPC reference
```jsonl
// Send:    {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {...}}
// Receive: {"jsonrpc": "2.0", "id": 1, "result": {...}}
// Send:    {"jsonrpc": "2.0", "id": 2, "method": "tools/list"}
// Receive: {"jsonrpc": "2.0", "id": 2, "result": {"tools": [...]}}
// Send:    {"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "list_recent_tickets", "arguments": {}}}
// Receive: {"jsonrpc": "2.0", "id": 3, "result": {"content": [...]}}
```
