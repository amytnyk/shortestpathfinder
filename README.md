# Shortest Path Problem

[![Pylint](https://github.com/amytnyk/shortestpathfinder/actions/workflows/pylint.yml/badge.svg)](https://github.com/amytnyk/shortestpathfinder/actions/workflows/pylint.yml)
[![Tests](https://github.com/amytnyk/shortestpathfinder/actions/workflows/tests.yml/badge.svg)](https://github.com/amytnyk/shortestpathfinder/actions/workflows/tests.yml)


To generate test:
```
python3.9 ./generator/generator.py tests/test.txt --rows 500 --cols 500 --end_row 499 --end_col 499
```

To run python version:
```
python3.9 ./python/finder.py tests/test.txt results/result_py.txt
```

The following command would print nothing if results are equal:
```
diff results/result_py.txt results/result_cpp.txt
```



This app was developed by a team of CS students at UCU.