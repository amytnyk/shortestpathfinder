Shortest Path Problem

To generate test:
```
python3 ./generator/generator.py tests/test.txt --rows 500 --cols 500 --end_row 499 --end_col 499
```

To run python version:
```
python3 ./python/finder.py tests/test.txt results/result_py.txt
```

To run c++ version:
```
g++ -o cpp/finder.o cpp/finder.cpp cpp/binary_heap.cpp -std=c++17; ./cpp/finder.o tests/test.txt results/result_cpp.txt
```

The following command would print nothing if results are equal:
```
diff results/result_py.txt results/result_cpp.txt
```