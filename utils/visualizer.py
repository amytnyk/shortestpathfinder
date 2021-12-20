import plotly.graph_objects as go
import argparse


def read_surface(path: str) -> list[list[float]]:
    with open(path, 'r') as file:
        lines = file.read().split('\n')
        arr = []
        for line in lines[3:]:
            if line:
                arr.append(list(map(float, filter(len, line.split(' ')))))
    return arr


def read_path(path: str) -> list[tuple[int, int]]:
    with open(path, 'r') as file:
        loc = {}
        exec(f"_, path = {file.read()}", globals(), loc)
        return loc["path"]


def plot(surface: list[list[float]], path=list[tuple[int, int]]):
    fig = go.Figure(data=[go.Surface(z=surface)])
    x, y = map(lambda x: x[1], path), map(lambda x: x[0], path)
    z = map(lambda x: surface[x[0]][x[1]], path)
    fig.add_scatter3d(x=list(x), y=list(y), z=list(z))
    fig.update_layout(title='Surface', autosize=True, scene = {"aspectmode": "data", "aspectratio": {"x": 1, "y": 1, "z": 1}})
    fig.show()


def visualize(test_path: str, result_path: str):
    plot(read_surface(test_path), read_path(result_path))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("test", help="path to test")
    parser.add_argument("result", help="path to result")
    
    args = parser.parse_args()
    visualize(args.test, args.result)


if __name__ == "__main__":
    main()