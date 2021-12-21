"""
Unittests for modules __a_star__, __dijkstra__ and __finder__
"""

import unittest
from core.a_star import find_shortest_path as fsp_ast
from core.dijkstra import find_shortest_path as fsp_dij


class TestA_star(unittest.TestCase):
    def test_fsp_ast(self):
        result_tuple = fsp_ast([
            [0, 1, 4, 5], [2, 3, 6, 6], [5, 2, 6, 7], [7, 4, 5, 6]
            ], 1, (0, 0), (3, 3))
        distance = result_tuple[0]
        path = result_tuple[1]
        needed_path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertAlmostEqual(distance, 10.128990204491961)
        self.assertEqual(path, needed_path)


class TestDijkstra(unittest.TestCase):
    def test_fsp_dij(self):
        result_tuple = fsp_dij([
            [0, 1, 4, 5], [2, 3, 6, 6], [5, 2, 6, 7], [7, 4, 5, 6]
            ], 1, (0, 0), (3, 3))
        distance = result_tuple[0]
        path = result_tuple[1]
        needed_path = [(0, 0), (0, 1), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
        self.assertAlmostEqual(distance, 10.128990204491961)
        self.assertEqual(path, needed_path)


if __name__ == '__main__':
    unittest.main()