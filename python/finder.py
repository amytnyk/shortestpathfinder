"""
Module for finding shortest path between two points in graph
Time complexity: O(V*log(v)), where v - number of vertices
"""
import math
import argparse
from typing import Tuple, List
from binary_heap import BinaryHeap

Point = Tuple[int, int]


def find_shortest_path(heights: List[List[float]], step: float,
                       point1: Point,
                       point2: Point) -> Tuple[float, List[Tuple[int, int]]]:
    rows = len(heights)
    cols = len(heights[0])

    heap = BinaryHeap()
    heap.push((0., point1))

    MAX = 10000000000.0
    not_visited = ((-1, -1), MAX, False)
    parents = [[not_visited for _ in range(cols)] for _ in range(rows)]
    parents[point1[0]][point1[1]] = ((0, 0), 0., True)

    while heap:
        dist, [py, px] = heap.pop()
        if (py, px) == point2:
            break
        parents[py][px] = (parents[py][px][0], dist, True)
        for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            y = py + dy
            x = px + dx
            if 0 <= y < rows and 0 <= x < cols:
                height_diff = heights[py][px] - heights[y][x]
                new_dist = dist + math.sqrt(step ** 2 + height_diff ** 2)

                if not parents[y][x][2] and parents[y][x][1] > new_dist:
                    parents[y][x] = ((py, px), new_dist, False)
                    heap.push((new_dist, (y, x)))

    path = [point2]
    while path[-1] != point1:
        path.append(parents[path[-1][0]][path[-1][1]][0])
    return parents[path[0][0]][path[0][1]][1], path[::-1]


def run_test(path_to_test: str, dst: str):
    arr = []
    with open(path_to_test, 'r', encoding='utf-8') as f:
        lines = f.read().split('\n')
        start = tuple(map(int, lines[0].split(' ')))[::-1]
        end = tuple(map(int, lines[1].split(' ')))[::-1]
        step = float(lines[2])
        
        for line in lines[4:]:
            if line:
                arr.append(list(map(float, filter(len, line.split(' ')))))
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(str(find_shortest_path(arr, step, start, end)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="path to test")
    parser.add_argument("dst", help="dest path")
    args = parser.parse_args()
    run_test(args.test, args.dst)


if __name__ == "__main__":
    main()
