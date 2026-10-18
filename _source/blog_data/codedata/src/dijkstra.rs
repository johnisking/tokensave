use std::cmp::Reverse;
use std::collections::{BTreeMap, BinaryHeap, HashMap};

const EDGES: [(&str, &str, u32); 9] = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 1), ("B", "D", 5), ("C", "D", 8),
    ("C", "E", 10), ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
];

fn build_graph() -> HashMap<&'static str, Vec<(&'static str, u32)>> {
    let mut graph: HashMap<&str, Vec<(&str, u32)>> = HashMap::new();
    for &(a, b, weight) in EDGES.iter() {
        graph.entry(a).or_default().push((b, weight));
        graph.entry(b).or_default().push((a, weight));
    }
    graph
}

fn dijkstra<'a>(
    graph: &HashMap<&'a str, Vec<(&'a str, u32)>>,
    start: &'a str,
) -> (BTreeMap<&'a str, u32>, HashMap<&'a str, &'a str>) {
    let mut dist: BTreeMap<&str, u32> = graph.keys().map(|&node| (node, u32::MAX)).collect();
    let mut prev = HashMap::new();
    dist.insert(start, 0);
    let mut queue = BinaryHeap::new();
    queue.push(Reverse((0, start)));
    while let Some(Reverse((d, node))) = queue.pop() {
        if d > dist[node] {
            continue;
        }
        for &(neighbor, weight) in &graph[node] {
            let nd = d + weight;
            if nd < dist[neighbor] {
                dist.insert(neighbor, nd);
                prev.insert(neighbor, node);
                queue.push(Reverse((nd, neighbor)));
            }
        }
    }
    (dist, prev)
}

fn main() {
    let graph = build_graph();
    let (dist, prev) = dijkstra(&graph, "A");
    for (node, d) in &dist {
        println!("{}: {}", node, d);
    }
    let mut path = vec!["F"];
    while *path.last().unwrap() != "A" {
        path.push(prev[path.last().unwrap()]);
    }
    path.reverse();
    println!("Path: {}", path.join(" -> "));
}
