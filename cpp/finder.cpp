#include <bits/stdc++.h>
#include "defs.hpp"
#include "binary_heap.hpp"

using namespace std;

pair<double, vector<Vec2>> find_shortest_path(const vector<vector<double>> &heights, const Vec2 &start, const Vec2 &end, double step) {
    size_t rows = heights.size();
    size_t cols = heights[0].size();

    auto heap = BinaryHeap<Node>();
    heap.push({0., start});

    double MAX = 10000000000.0;
    Record not_visited = {{MAX, {-1, -1}}, false};
    vector<vector<Record>> parents(rows, vector<Record>(cols, not_visited));
    parents[start.y][start.x] = {{0, start}, true};

    while (!heap.empty()) {
        auto node = heap.pop();
        if (node.point == end)
            break;
        parents[node.point.y][node.point.x].visited = true;
        int neighbours[4][2] = {{0,  1},
                                {0,  -1},
                                {1,  0},
                                {-1, 0}};
        for (auto[dx, dy]: neighbours) {
            int x = node.point.x + dx;
            int y = node.point.y + dy;

            if (0 <= x && x < cols && 0 <= y && y < rows) {
                double height_diff = heights[node.point.y][node.point.x] - heights[y][x];
                double new_dist = node.distance + sqrt(step * step + height_diff * height_diff);

                if (!parents[y][x].visited && parents[y][x].node.distance > new_dist) {
                    parents[y][x] = {{new_dist, node.point}, false};
                    heap.push({new_dist, {x, y}});
                }
            }
        }
    }
    vector<Vec2> path = {end};
    while (path[path.size() - 1] != start)
        path.push_back(parents[path[path.size() - 1].y][path[path.size() - 1].x].node.point);
    auto dist = parents[path[0].y][path[0].x].node.distance;
    reverse(path.begin(), path.end());
    return {dist, path};
}

int main(int argc, char** argv) {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    freopen(argv[1], "r", stdin);
    Vec2 start, end;
    cin >> start.x >> start.y >> end.x >> end.y;
    int step;
    cin >> step;
    int rows, cols;
    cin >> rows >> cols;
    vector<vector<double>> heights(rows, vector<double>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++)
            cin >> heights[i][j];
    }
    fclose(stdin);
    auto arr = find_shortest_path(heights, start, end, step);

    freopen(argv[2], "w", stdout);
    cout <<  "(" << fixed << setprecision(10) << arr.first << ", [";
    for (size_t i = 0; i < arr.second.size(); i++) {
        cout << "(" << arr.second[i].y << ", " << arr.second[i].x << ")";
        if (i != arr.second.size() - 1)
            cout << ", ";
    }
    cout << "])";
    cout.flush();
    fclose(stdout);
    return 0;
}
