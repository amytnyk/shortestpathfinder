"""
Module for finding shortest path between two points in graph
Time complexity: O(V*log(v)), where v - number of vertices
"""
import argparse
import time
import dijkstra
import a_star


def run_test(path_to_test: str, dst: str, func: callable):
    with open(path_to_test, 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
        size, step = tuple(map(int, lines[0].split()))
        start = tuple(map(int, lines[1].split()))
        end = tuple(map(int, lines[2].split()))
        
        arr = []
        for line in lines[3:]:
            if line:
                arr.append(list(map(float, filter(len, line.split(' ')))))
        print('Finished reading data')

        start_time = time.time()
        result = func(arr, step, start, end)
        print(f"Time elapsed: {time.time() - start_time}")

        with open(dst, 'w', encoding='utf-8') as f:
            f.write(str(result))
        


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="path to test")
    parser.add_argument("dst", help="dest path")
    parser.add_argument("--visualize", action='store_true')
    parser.add_argument("--dijkstra", action='store_true')
    args = parser.parse_args()
    run_test(args.test, args.dst, dijkstra.find_shortest_path if args.dijkstra else a_star.find_shortest_path)
    if args.visualize:
        from utils.visualizer import visualize
        visualize(args.test, args.dst)


if __name__ == "__main__":
    main()
