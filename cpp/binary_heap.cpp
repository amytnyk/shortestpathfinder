#include "binary_heap.hpp"

template class BinaryHeap<Node>;

template<typename T>
void BinaryHeap<T>::push(const T &val)
{
    heap.push_back(val);
    shift_up();
}

template<typename T>
bool BinaryHeap<T>::empty() const
{
    return heap.empty();
}

template<typename T>
T BinaryHeap<T>::top() const
{
    return heap[0];
}

template<typename T>
T BinaryHeap<T>::pop()
{
    T val = top();
    heap[0] = heap[heap.size() - 1];
    heap.pop_back();
    shift_down();
    return val;
}

template<typename T>
void BinaryHeap<T>::swap(int idx1, int idx2)
{
    std::swap(heap[idx1], heap[idx2]);
}

template<typename T>
void BinaryHeap<T>::shift_up()
{
    int idx = heap.size() - 1;

    while (idx > 0)
    {
        int parent = (idx - 1) >> 1;
        if (heap[parent] > heap[idx])
        {
            this->swap(parent, idx);
            idx = parent;
        }
        else
            break;
    }
}

template<typename T>
void BinaryHeap<T>::shift_down()
{
    int idx = 0;

    while (2 * idx + 1 < heap.size())
    {
        int left = 2 * idx + 1;
        int right = left + 1;
        T val = heap[idx];
        T left_val = heap[left];

        if (right >= heap.size())
        {
            if (val < left_val)
                break;
            else
            {
                this->swap(idx, left);
                idx = left;
            }
        }
        else
        {
            T right_val = heap[right];
            if (val < min(left_val, right_val))
                break;
            else
            {
                if (left_val > right_val)
                {
                    this->swap(idx, right);
                    idx = right;
                }
                else
                {
                    this->swap(idx, left);
                    idx = left;
                }
            }
        }
    }
}