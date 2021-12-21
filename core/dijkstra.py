"""
Module for finding shortest path between two points in graph using Dijkstra algorithm
Time complexity: O(V*log(v)), where v - number of vertices
"""
import heapq
from math import sqrt, inf

Point = tuple[int, int]

def find_shortest_path(heights: list[list[float]], step: float,
                       point1: Point,
                       point2: Point) -> tuple[float, list[Point]]:
    """
    Calculates shortest path between two points using Dijkstra algorithm
    """
    rows = len(heights)
    cols = len(heights[0])

    heap = []
    heapq.heappush(heap, [0., point1])

    parents = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]
    distances = [[inf for _ in range(cols)] for _ in range(rows)]

    parents[point1[0]][point1[1]] = (0, 0)
    distances[point1[0]][point1[1]] = 0

    while heap:
        dist, [py, px] = heapq.heappop(heap)
        if (py, px) == point2:
            break
        if dist > distances[py][px]:
            continue
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            y = py + dy
            x = px + dx
            if 0 <= y < rows and 0 <= x < cols:
                height_diff = heights[py][px] - heights[y][x]
                new_dist = dist + sqrt(step * step + height_diff * height_diff)
                if distances[y][x] > new_dist:
                    parents[y][x] = (py, px)
                    distances[y][x] = new_dist
                    heapq.heappush(heap, [new_dist, (y, x)])

    path = [point2]
    while path[-1] != point1:
        path.append(parents[path[-1][0]][path[-1][1]])
    return distances[point2[0]][point2[1]], path[::-1]
