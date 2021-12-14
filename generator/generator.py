import argparse
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dst")
    parser.add_argument("--start_col", default=10, type=int)
    parser.add_argument("--start_row", default=10, type=int)
    parser.add_argument("--end_col", default=480, type=int)
    parser.add_argument("--end_row", default=480, type=int)
    parser.add_argument("--step", default=10, type=float)
    parser.add_argument("--rows", default=500, type=int)
    parser.add_argument("--cols", default=500, type=int)
    parser.add_argument("--min_height", default=-2500, type=float)
    parser.add_argument("--max_height", default=2500, type=float)
    args = parser.parse_args()

    with open(args.dst, 'w', encoding="utf-8") as f:
        f.write(f"{args.start_col} {args.start_row}\n")
        f.write(f"{args.end_col} {args.end_row}\n")
        f.write(f"{args.step}\n")
        f.write(f"{args.rows} {args.cols}\n")

        for _ in range(args.rows):
            for _ in range(args.cols):
                f.write(f"{random.uniform(args.min_height, args.max_height)} ")
            f.write("\n")


if __name__ == "__main__":
    main()