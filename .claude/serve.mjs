import http from "node:http";
import { readFile } from "node:fs/promises";
import path from "node:path";

const ROOT = "/Users/chintu/Documents/GitHub/Dishanth234";
const TYPES = { ".html": "text/html", ".svg": "image/svg+xml", ".png": "image/png", ".json": "application/json" };

http.createServer(async (req, res) => {
  try {
    const urlPath = decodeURIComponent(new URL(req.url, "http://x").pathname);
    let rel = urlPath === "/" ? "/preview.html" : urlPath;
    const file = path.normalize(path.join(ROOT, rel));
    if (!file.startsWith(ROOT)) throw new Error("bad path");
    const data = await readFile(file);
    res.writeHead(200, { "content-type": TYPES[path.extname(file)] ?? "application/octet-stream" });
    res.end(data);
  } catch {
    res.writeHead(404); res.end("not found");
  }
}).listen(8642, () => console.log("serving on 8642"));
