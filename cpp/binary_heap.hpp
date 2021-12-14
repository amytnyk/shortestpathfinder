#pragma once
#include <vector>
#include "defs.hpp"
using namespace std;

template<typename T>
class BinaryHeap {
public:
    vector<T> heap;

    void push(const T& val);
    bool empty() const;
    T top() const;
    T pop();
    void swap(int idx1, int idx2);
private:
    void shift_up();
    void shift_down();
};
