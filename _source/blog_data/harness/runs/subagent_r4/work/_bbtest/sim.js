const fs = require("fs");
const h = fs.readFileSync(process.argv[2], "utf8");
let src = h.match(/<script>([\s\S]*?)<\/script>/)[1];
fs.writeFileSync(__dirname + "/bb.js", src);
src = src.replace(/requestAnimationFrame\(frame\);\s*\}\)\(\);\s*$/,
  "globalThis.__g={get state(){return state},get score(){return score},get lives(){return lives},get level(){return levelIndex},ball,paddle,bricks:()=>bricks,update,render,primaryAction};\n})();");
if (!src.includes("__g")) throw new Error("hook failed");
const noop = () => {};
const ctx = new Proxy({}, { get: (t, k) => k === "createLinearGradient" ? () => ({ addColorStop: noop }) : (t[k] !== undefined ? t[k] : noop), set: (t, k, v) => { t[k] = v; return true; } });
globalThis.window = { addEventListener: noop };
globalThis.document = { getElementById: () => ({ width: 800, height: 600, getContext: () => ctx, addEventListener: noop, getBoundingClientRect: () => ({ left: 0, width: 800 }) }) };
globalThis.requestAnimationFrame = noop;
eval(src);
const g = globalThis.__g;
g.render();
g.primaryAction(); g.primaryAction();
let t = 0, inside = 0;
while (t < 900 && g.state !== "win" && g.state !== "gameover") {
  g.paddle.x = g.ball.x - g.paddle.w / 2 + Math.sin(t * 3) * 40;
  g.paddle.x = Math.max(0, Math.min(800 - g.paddle.w, g.paddle.x));
  if (g.state === "ready") g.primaryAction();
  g.update(1 / 60); g.render(); t += 1 / 60;
  for (const b of g.bricks()) if (b.alive) {
    const cx = Math.max(b.x, Math.min(g.ball.x, b.x + b.w)), cy = Math.max(b.y, Math.min(g.ball.y, b.y + b.h));
    if (Math.hypot(g.ball.x - cx, g.ball.y - cy) < g.ball.r - 0.5) inside++;
  }
}
console.log("autopilot:", g.state, "score", g.score, "lives", g.lives, "level", g.level + 1, "t", t.toFixed(1), "insideBrickFrames", inside);
g.primaryAction(); console.log("restart:", g.state, g.score, g.lives, g.level + 1);
g.primaryAction(); t = 0;
while (g.state !== "gameover" && t < 120) { g.paddle.x = g.ball.x > 400 ? 0 : 690; if (g.state === "ready") g.primaryAction(); g.update(1 / 60); g.render(); t += 1 / 60; }
console.log("miss test:", g.state, "lives", g.lives, "score", g.score);
