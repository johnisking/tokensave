EDGES = [
  ['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8],
  ['C', 'E', 10], ['D', 'E', 2], ['D', 'F', 6], ['E', 'F', 3]
].freeze

def build_graph(edges)
  graph = Hash.new { |hash, key| hash[key] = [] }
  edges.each do |a, b, weight|
    graph[a] << [b, weight]
    graph[b] << [a, weight]
  end
  graph
end

def dijkstra(graph, start)
  dist = graph.keys.to_h { |node| [node, Float::INFINITY] }
  prev = {}
  dist[start] = 0
  queue = [[0, start]]
  until queue.empty?
    d, node = queue.min_by(&:first)
    queue.delete([d, node])
    next if d > dist[node]

    graph[node].each do |neighbor, weight|
      nd = d + weight
      next unless nd < dist[neighbor]

      dist[neighbor] = nd
      prev[neighbor] = node
      queue << [nd, neighbor]
    end
  end
  [dist, prev]
end

def path_to(prev, start, target)
  path = [target]
  path << prev[path.last] until path.last == start
  path.reverse
end

graph = build_graph(EDGES)
dist, prev = dijkstra(graph, 'A')
dist.keys.sort.each { |node| puts "#{node}: #{dist[node]}" }
puts "Path: #{path_to(prev, 'A', 'F').join(' -> ')}"
