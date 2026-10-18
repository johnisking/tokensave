#include <limits.h>
#include <stdbool.h>
#include <stdio.h>

#define N 6

static const char NAMES[N] = {'A', 'B', 'C', 'D', 'E', 'F'};

static const int EDGES[][3] = {
    {0, 1, 4}, {0, 2, 2}, {1, 2, 1}, {1, 3, 5}, {2, 3, 8},
    {2, 4, 10}, {3, 4, 2}, {3, 5, 6}, {4, 5, 3},
};

int main(void) {
    int graph[N][N] = {0};
    int edge_count = sizeof(EDGES) / sizeof(EDGES[0]);
    for (int i = 0; i < edge_count; i++) {
        graph[EDGES[i][0]][EDGES[i][1]] = EDGES[i][2];
        graph[EDGES[i][1]][EDGES[i][0]] = EDGES[i][2];
    }
    int dist[N];
    int prev[N];
    bool done[N] = {false};
    for (int i = 0; i < N; i++) {
        dist[i] = INT_MAX;
        prev[i] = -1;
    }
    dist[0] = 0;
    for (int round = 0; round < N; round++) {
        int node = -1;
        for (int i = 0; i < N; i++) {
            if (!done[i] && (node == -1 || dist[i] < dist[node])) {
                node = i;
            }
        }
        if (dist[node] == INT_MAX) {
            break;
        }
        done[node] = true;
        for (int neighbor = 0; neighbor < N; neighbor++) {
            int weight = graph[node][neighbor];
            if (weight > 0 && dist[node] + weight < dist[neighbor]) {
                dist[neighbor] = dist[node] + weight;
                prev[neighbor] = node;
            }
        }
    }
    for (int i = 0; i < N; i++) {
        printf("%c: %d\n", NAMES[i], dist[i]);
    }
    int path[N];
    int length = 0;
    for (int node = 5; node != -1; node = prev[node]) {
        path[length++] = node;
    }
    printf("Path: ");
    for (int i = length - 1; i >= 0; i--) {
        printf("%c%s", NAMES[path[i]], i > 0 ? " -> " : "");
    }
    printf("\n");
    return 0;
}
