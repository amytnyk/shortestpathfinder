"""
Module for finding shortest path between two points in graph using A* algorithm
Time complexity: O(V*log(v)), where v - number of vertices
"""
from math import sqrt, inf, fabs
import heapq

Point = tuple[int, int]


def manhattan_distance(point1: Point, point2: Point):
    """
    Returns manhattan distance between 2 points
    """
    return fabs(point2[0] - point1[0]) + fabs(point2[1] - point1[1])


def find_shortest_path(heights: list[list[float]], step: float,
                       point1: Point,
                       point2: Point) -> tuple[float, list[Point]]:
    """
    Calculates shortest path between two points using A* algorithm
    """
    rows = len(heights)
    cols = len(heights[0])

    heap = []
    heapq.heappush(heap, [0., point1])

    parents = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]
    distances = [[inf for _ in range(cols)] for _ in range(rows)]
    hdistances = [[inf for _ in range(cols)] for _ in range(rows)]

    parents[point1[0]][point1[1]] = (0, 0)
    distances[point1[0]][point1[1]] = 0
    hdistances[point1[0]][point1[1]] = step * manhattan_distance(point1, point2)

    while heap:
        dist, [py, px] = heapq.heappop(heap)
        if (py, px) == point2:
            break
        if dist > hdistances[py][px]:
            continue
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            y = py + dy
            x = px + dx
            if 0 <= y < rows and 0 <= x < cols:
                height_diff = heights[py][px] - heights[y][x]
                new_dist = distances[py][px] + sqrt(step * step + height_diff * height_diff)
                if distances[y][x] > new_dist:
                    parents[y][x] = (py, px)
                    distances[y][x] = new_dist
                    new_dist += step * manhattan_distance(point2, (y, x))
                    hdistances[y][x] = new_dist
                    heapq.heappush(heap, [new_dist, (y, x)])

    path = [point2]
    while path[-1] != point1:
        path.append(parents[path[-1][0]][path[-1][1]])
    return distances[point2[0]][point2[1]], path[::-1]
