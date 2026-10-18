<?php

const EDGES = [
    ['A', 'B', 4], ['A', 'C', 2], ['B', 'C', 1], ['B', 'D', 5], ['C', 'D', 8],
    ['C', 'E', 10], ['D', 'E', 2], ['D', 'F', 6], ['E', 'F', 3],
];

function buildGraph(array $edges): array
{
    $graph = [];
    foreach ($edges as [$a, $b, $weight]) {
        $graph[$a][] = [$b, $weight];
        $graph[$b][] = [$a, $weight];
    }
    return $graph;
}

function dijkstra(array $graph, string $start): array
{
    $dist = array_fill_keys(array_keys($graph), PHP_INT_MAX);
    $prev = [];
    $dist[$start] = 0;
    $queue = new SplPriorityQueue();
    $queue->setExtractFlags(SplPriorityQueue::EXTR_BOTH);
    $queue->insert($start, 0);
    while (!$queue->isEmpty()) {
        ['data' => $node, 'priority' => $priority] = $queue->extract();
        $d = -$priority;
        if ($d > $dist[$node]) {
            continue;
        }
        foreach ($graph[$node] as [$neighbor, $weight]) {
            $nd = $d + $weight;
            if ($nd < $dist[$neighbor]) {
                $dist[$neighbor] = $nd;
                $prev[$neighbor] = $node;
                $queue->insert($neighbor, -$nd);
            }
        }
    }
    return [$dist, $prev];
}

function pathTo(array $prev, string $start, string $target): array
{
    $path = [$target];
    while (end($path) !== $start) {
        $path[] = $prev[end($path)];
    }
    return array_reverse($path);
}

$graph = buildGraph(EDGES);
[$dist, $prev] = dijkstra($graph, 'A');
ksort($dist);
foreach ($dist as $node => $d) {
    echo "$node: $d\n";
}
echo 'Path: ' . implode(' -> ', pathTo($prev, 'A', 'F')) . "\n";
