import argparse
from skimage import io
from skimage.color import rgb2gray


def h2t(path: str, min_height: float, max_height: float) -> tuple[int, list[list[float]]]:
    image = io.imread(path, as_gray=True)
    size, height = image.shape
    if size != height:
        raise 'Width should be equal to height'
    def pixel_to_height(pixel: float) -> float:
        return min_height + pixel * (max_height - min_height)

    return size, [[pixel_to_height(image[col, row]) for col in range(size)] for row in range(size)]


def main():
    parser = argparse.ArgumentParser(
        description='Converts white/black heightmap to test')
    parser.add_argument("image", help="path to heightmap")
    parser.add_argument("test", help="path to test")
    parser.add_argument("--max_height", type=int, default=2000)
    parser.add_argument("--min_height", type=int, default=-1000)
    parser.add_argument("--step", type=int, default=10)
    parser.add_argument("start_row", type=int)
    parser.add_argument("start_col", type=int)
    parser.add_argument("end_row", type=int)
    parser.add_argument("end_col", type=int)
    args = parser.parse_args()

    size, heightmap = h2t(args.image, args.min_height, args.max_height)

    def in_bounds(x): return 0 <= x < size
    if not all(map(in_bounds, [args.start_row, args.start_col, args.end_row, args.end_col])):
        raise 'Invalid options: coordinates are not in [0; size)'

    with open(args.test, 'w', encoding='utf-8') as file:
        file.write(f'{size} {args.step}\n')
        file.write(f'{args.start_row} {args.start_col}\n')
        file.write(f'{args.end_row} {args.end_row}\n')
        file.write('\n'.join(map(lambda row: ' '.join(map(str, row)), heightmap)))


if __name__ == "__main__":
    main()
