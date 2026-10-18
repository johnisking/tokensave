#include <algorithm>
#include <climits>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <tuple>
#include <utility>
#include <vector>

using Graph = std::map<std::string, std::vector<std::pair<std::string, int>>>;

const std::vector<std::tuple<std::string, std::string, int>> EDGES = {
    {"A", "B", 4}, {"A", "C", 2}, {"B", "C", 1}, {"B", "D", 5}, {"C", "D", 8},
    {"C", "E", 10}, {"D", "E", 2}, {"D", "F", 6}, {"E", "F", 3},
};

Graph buildGraph() {
    Graph graph;
    for (const auto& [a, b, weight] : EDGES) {
        graph[a].push_back({b, weight});
        graph[b].push_back({a, weight});
    }
    return graph;
}

int main() {
    Graph graph = buildGraph();
    std::map<std::string, int> dist;
    std::map<std::string, std::string> prev;
    for (const auto& [node, edges] : graph) {
        dist[node] = INT_MAX;
    }
    dist["A"] = 0;
    using Entry = std::pair<int, std::string>;
    std::priority_queue<Entry, std::vector<Entry>, std::greater<Entry>> queue;
    queue.push({0, "A"});
    while (!queue.empty()) {
        auto [d, node] = queue.top();
        queue.pop();
        if (d > dist[node]) {
            continue;
        }
        for (const auto& [neighbor, weight] : graph[node]) {
            int nd = d + weight;
            if (nd < dist[neighbor]) {
                dist[neighbor] = nd;
                prev[neighbor] = node;
                queue.push({nd, neighbor});
            }
        }
    }
    for (const auto& [node, d] : dist) {
        std::cout << node << ": " << d << "\n";
    }
    std::vector<std::string> path = {"F"};
    while (path.back() != "A") {
        path.push_back(prev[path.back()]);
    }
    std::reverse(path.begin(), path.end());
    std::cout << "Path: ";
    for (size_t i = 0; i < path.size(); ++i) {
        std::cout << (i > 0 ? " -> " : "") << path[i];
    }
    std::cout << "\n";
    return 0;
}
