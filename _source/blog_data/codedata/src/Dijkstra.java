import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.TreeMap;

public class Dijkstra {
    record Edge(String to, int weight) {}

    record Entry(int dist, String node) {}

    static final Object[][] EDGES = {
        {"A", "B", 4}, {"A", "C", 2}, {"B", "C", 1}, {"B", "D", 5}, {"C", "D", 8},
        {"C", "E", 10}, {"D", "E", 2}, {"D", "F", 6}, {"E", "F", 3},
    };

    static Map<String, List<Edge>> buildGraph() {
        Map<String, List<Edge>> graph = new HashMap<>();
        for (Object[] e : EDGES) {
            String a = (String) e[0];
            String b = (String) e[1];
            int weight = (Integer) e[2];
            graph.computeIfAbsent(a, k -> new ArrayList<>()).add(new Edge(b, weight));
            graph.computeIfAbsent(b, k -> new ArrayList<>()).add(new Edge(a, weight));
        }
        return graph;
    }

    public static void main(String[] args) {
        Map<String, List<Edge>> graph = buildGraph();
        Map<String, Integer> dist = new TreeMap<>();
        Map<String, String> prev = new HashMap<>();
        for (String node : graph.keySet()) {
            dist.put(node, Integer.MAX_VALUE);
        }
        dist.put("A", 0);
        PriorityQueue<Entry> queue = new PriorityQueue<>((x, y) -> Integer.compare(x.dist(), y.dist()));
        queue.add(new Entry(0, "A"));
        while (!queue.isEmpty()) {
            Entry current = queue.poll();
            if (current.dist() > dist.get(current.node())) {
                continue;
            }
            for (Edge edge : graph.get(current.node())) {
                int nd = current.dist() + edge.weight();
                if (nd < dist.get(edge.to())) {
                    dist.put(edge.to(), nd);
                    prev.put(edge.to(), current.node());
                    queue.add(new Entry(nd, edge.to()));
                }
            }
        }
        for (Map.Entry<String, Integer> entry : dist.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        List<String> path = new ArrayList<>();
        path.add("F");
        while (!path.get(path.size() - 1).equals("A")) {
            path.add(prev.get(path.get(path.size() - 1)));
        }
        Collections.reverse(path);
        System.out.println("Path: " + String.join(" -> ", path));
    }
}
