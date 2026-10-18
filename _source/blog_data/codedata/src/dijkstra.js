const EDGES = [
  ["A", "B", 4], ["A", "C", 2], ["B", "C", 1], ["B", "D", 5], ["C", "D", 8],
  ["C", "E", 10], ["D", "E", 2], ["D", "F", 6], ["E", "F", 3],
];

function buildGraph(edges) {
  const graph = new Map();
  for (const [a, b, weight] of edges) {
    if (!graph.has(a)) graph.set(a, []);
    if (!graph.has(b)) graph.set(b, []);
    graph.get(a).push([b, weight]);
    graph.get(b).push([a, weight]);
  }
  return graph;
}

function dijkstra(graph, start) {
  const dist = new Map();
  const prev = new Map();
  for (const node of graph.keys()) dist.set(node, Infinity);
  dist.set(start, 0);
  const queue = [[0, start]];
  while (queue.length > 0) {
    queue.sort((x, y) => x[0] - y[0]);
    const [d, node] = queue.shift();
    if (d > dist.get(node)) continue;
    for (const [neighbor, weight] of graph.get(node)) {
      const nd = d + weight;
      if (nd < dist.get(neighbor)) {
        dist.set(neighbor, nd);
        prev.set(neighbor, node);
        queue.push([nd, neighbor]);
      }
    }
  }
  return { dist, prev };
}

function pathTo(prev, start, target) {
  const path = [target];
  while (path[path.length - 1] !== start) {
    path.push(prev.get(path[path.length - 1]));
  }
  return path.reverse();
}

function main() {
  const graph = buildGraph(EDGES);
  const { dist, prev } = dijkstra(graph, "A");
  for (const node of [...dist.keys()].sort()) {
    console.log(`${node}: ${dist.get(node)}`);
  }
  console.log("Path:", pathTo(prev, "A", "F").join(" -> "));
}

main();
