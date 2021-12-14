"""
Binary heap module
Binary heap aka Priority queue
"""
from typing import TypeVar, Optional

T = TypeVar("T")


class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: T):
        """
        Inserts element to heap
        Time complexity: O(logn)
        """
        self.heap.append(val)
        self.shift_up()

    def empty(self) -> bool:
        return len(self.heap) == 0

    def top(self) -> Optional[T]:
        """
        Return top element from heap
        Time complexity: O(1)
        """
        if self.empty():
            return None
        else:
            return self.heap[0]

    def pop(self) -> Optional[T]:
        """
        Pops element from heap
        Time complexity: O(logn)
        """
        if self.empty():
            return None
        val = self.top()
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.shift_down()
        return val

    def swap(self, idx1: int, idx2: int):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def shift_up(self):
        idx = len(self.heap) - 1

        while idx > 0:
            parent = (idx - 1) >> 1
            if self.heap[parent] > self.heap[idx]:
                self.swap(parent, idx)
                idx = parent
            else:
                break

    def shift_down(self):
        idx = 0

        while (left := 2 * idx + 1) < len(self.heap):
            left_val = self.heap[left]
            val = self.heap[idx]
            right = left + 1

            if right >= len(self.heap):
                if val >= left_val:
                    self.swap(idx, left)
                    idx = left
                else:
                    break
            else:
                right_val = self.heap[right]
                if val >= min(left_val, right_val):
                    if left_val <= right_val:
                        self.swap(idx, left)
                        idx = left
                    else:
                        self.swap(idx, right)
                        idx = right
                else:
                    break

    def __bool__(self):
        return not self.empty()
