import argparse
import noise


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dst")
    parser.add_argument("--start_col", default=10, type=int)
    parser.add_argument("--start_row", default=10, type=int)
    parser.add_argument("--end_col", default=480, type=int)
    parser.add_argument("--end_row", default=480, type=int)
    parser.add_argument("--step", default=10, type=float)
    parser.add_argument("--size", default=500, type=int)
    parser.add_argument("--min_height", default=-1000, type=float)
    parser.add_argument("--max_height", default=5000, type=float)
    args = parser.parse_args()

    def in_bounds(x): return 0 <= x < args.size
    if not all(map(in_bounds, [args.start_row, args.start_col, args.end_row, args.end_col])):
        raise 'Invalid options: coordinates are not in [0; size)'

    with open(args.dst, 'w', encoding="utf-8") as file:
        file.write(f"{args.size} {args.step}\n")
        file.write(f"{args.start_col} {args.start_row}\n")
        file.write(f"{args.end_col} {args.end_row}\n")

        heights = [[0 for _ in range(args.size)] for _ in range(args.size)]
        for i in range(args.size):
            for j in range(args.size):
                heights[i][j] = float(noise.pnoise2(i / 100, j / 100, 
                                    octaves=10, 
                                    persistence=0.5,
                                    lacunarity=2, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=42))
        for i in range(args.size):
            file.write(f"{' '.join(map(str, heights[i]))}\n")


if __name__ == "__main__":
    main()