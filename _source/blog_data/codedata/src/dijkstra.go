package main

import (
	"container/heap"
	"fmt"
	"math"
	"sort"
	"strings"
)

type Edge struct {
	To     string
	Weight int
}

type Entry struct {
	Dist int
	Node string
}

type Queue []Entry

func (q Queue) Len() int            { return len(q) }
func (q Queue) Less(i, j int) bool  { return q[i].Dist < q[j].Dist }
func (q Queue) Swap(i, j int)       { q[i], q[j] = q[j], q[i] }
func (q *Queue) Push(x interface{}) { *q = append(*q, x.(Entry)) }
func (q *Queue) Pop() interface{} {
	old := *q
	n := len(old)
	item := old[n-1]
	*q = old[:n-1]
	return item
}

var edges = []struct {
	A, B   string
	Weight int
}{
	{"A", "B", 4}, {"A", "C", 2}, {"B", "C", 1}, {"B", "D", 5}, {"C", "D", 8},
	{"C", "E", 10}, {"D", "E", 2}, {"D", "F", 6}, {"E", "F", 3},
}

func buildGraph() map[string][]Edge {
	graph := make(map[string][]Edge)
	for _, e := range edges {
		graph[e.A] = append(graph[e.A], Edge{e.B, e.Weight})
		graph[e.B] = append(graph[e.B], Edge{e.A, e.Weight})
	}
	return graph
}

func dijkstra(graph map[string][]Edge, start string) (map[string]int, map[string]string) {
	dist := make(map[string]int)
	prev := make(map[string]string)
	for node := range graph {
		dist[node] = math.MaxInt
	}
	dist[start] = 0
	q := &Queue{{0, start}}
	for q.Len() > 0 {
		current := heap.Pop(q).(Entry)
		if current.Dist > dist[current.Node] {
			continue
		}
		for _, edge := range graph[current.Node] {
			nd := current.Dist + edge.Weight
			if nd < dist[edge.To] {
				dist[edge.To] = nd
				prev[edge.To] = current.Node
				heap.Push(q, Entry{nd, edge.To})
			}
		}
	}
	return dist, prev
}

func main() {
	graph := buildGraph()
	dist, prev := dijkstra(graph, "A")
	nodes := make([]string, 0, len(dist))
	for node := range dist {
		nodes = append(nodes, node)
	}
	sort.Strings(nodes)
	for _, node := range nodes {
		fmt.Printf("%s: %d\n", node, dist[node])
	}
	path := []string{"F"}
	for path[len(path)-1] != "A" {
		path = append(path, prev[path[len(path)-1]])
	}
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	fmt.Println("Path:", strings.Join(path, " -> "))
}
