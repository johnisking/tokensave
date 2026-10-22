#!/usr/bin/env node
// snapshot-diet: an MCP proxy that keeps browser page snapshots out of your context.
// It wraps a browser MCP server (Playwright MCP, Chrome DevTools MCP), passes every tool through,
// and when a tool returns a very large page snapshot it sends back a short outline instead.
// The full snapshot stays in memory; the model can read any part of it with `snapshot_detail`.
//
// Usage: snapshot-diet [--max-chars 8000] [--keep-links 12] -- <upstream command> [args...]
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { ListToolsRequestSchema, CallToolRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import { outline, detail, isSnapshot } from "./slim.js";

const argv = process.argv.slice(2);
const sep = argv.indexOf("--");
if (sep < 0 || sep === argv.length - 1) {
  console.error("usage: snapshot-diet [--max-chars N] [--keep-links N] -- <upstream command> [args...]");
  process.exit(2);
}
const opts = { maxChars: 8000, keepLinks: 12 };
for (let i = 0; i < sep; i++) {
  if (argv[i] === "--max-chars") opts.maxChars = Number(argv[++i]);
  else if (argv[i] === "--keep-links") opts.keepLinks = Number(argv[++i]);
}
const [cmd, ...cmdArgs] = argv.slice(sep + 1);

const upstream = new Client({ name: "snapshot-diet", version: "0.1.0" });
await upstream.connect(new StdioClientTransport({ command: cmd, args: cmdArgs, stderr: "inherit" }));

let lastSnapshot = null; // full text of the most recent large snapshot

const DETAIL_TOOL = {
  name: "snapshot_detail",
  description:
    "Read part of the last page snapshot that snapshot-diet shortened. Pass `ref` (an element ref or uid from the outline, e.g. e123 or 1_45) " +
    "to get that element and everything inside it, or `query` to find text on the page with its surrounding section. Use this instead of taking a new full snapshot.",
  inputSchema: {
    type: "object",
    properties: {
      ref: { type: "string", description: "Element ref or uid shown in the outline" },
      query: { type: "string", description: "Text to find on the page (case-insensitive)" },
      max_chars: { type: "number", description: "Maximum characters to return (default 4000)" },
    },
  },
};

const server = new Server({ name: "snapshot-diet", version: "0.1.0" }, { capabilities: { tools: {} } });

server.setRequestHandler(ListToolsRequestSchema, async () => {
  const { tools } = await upstream.listTools();
  return { tools: [...tools, DETAIL_TOOL] };
});

server.setRequestHandler(CallToolRequestSchema, async (req) => {
  const { name, arguments: args = {} } = req.params;
  if (name === DETAIL_TOOL.name) {
    if (!lastSnapshot) return { content: [{ type: "text", text: "No shortened snapshot yet. Take a snapshot first." }] };
    return { content: [{ type: "text", text: detail(lastSnapshot, args, args.max_chars || 4000) }] };
  }
  const res = await upstream.callTool({ name, arguments: args });
  if (Array.isArray(res.content)) {
    res.content = res.content.map((c) => {
      if (c.type !== "text" || c.text.length <= opts.maxChars || !isSnapshot(c.text)) return c;
      lastSnapshot = c.text;
      const o = outline(c.text, opts);
      const note =
        `[snapshot-diet] The page snapshot was ${c.text.length.toLocaleString("en-US")} characters, so only an outline is shown ` +
        `(${o.length.toLocaleString("en-US")} characters): headings, form fields, buttons and links, with long text cut. ` +
        `Refs work as usual. To read a part of the page, call snapshot_detail with a ref or a text query.\n\n`;
      return { type: "text", text: note + o };
    });
  }
  return res;
});

await server.connect(new StdioServerTransport());
