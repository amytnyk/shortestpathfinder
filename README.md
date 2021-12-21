# Shortest Path Problem

[![Pylint](https://github.com/amytnyk/shortestpathfinder/actions/workflows/pylint.yml/badge.svg)](https://github.com/amytnyk/shortestpathfinder/actions/workflows/pylint.yml)
[![Tests](https://github.com/amytnyk/shortestpathfinder/actions/workflows/tests.yml/badge.svg)](https://github.com/amytnyk/shortestpathfinder/actions/workflows/tests.yml)

## Модуль dijkstra
### Ініціалізація
```python:core/dijkstra.py [16-26]
rows = len(heights)
cols = len(heights[0])

heap = []
heapq.heappush(heap, [0., point1])
parents = [[(-1, -1) for _ in range(cols)] for _ in range(rows]
distances = [[inf for _ in range(cols)] for _ in range(rows)]

parents[point1[0]][point1[1]] = (0, 0)
distances[point1[0]][point1[1]] = 0
```
* У distances[row][col] будемо зберігати найкоротшу відстань від початкової координати до (row, col), спочатку всі вершини містять нескінченність як індикатор того, що шлях ще не знайдений
* У parents[row][col] будемо зберігати координату вершини, із якої ми прийшли у (row, col), спочатку всі вершини містять (-1, -1) як індикатор того, що шлях ще не знайдений
* У структурі даних heap зберігатимемо вершини, які ми розглядаємо. Спочатку там міститься початкова вершина.
### Хід алгоритму
```python:core/dijkstra.py [28-43]
while heap:
       dist, [py, px] = heapq.heappop(heap)
       if (py, px) == point2:
           break
       if dist > distances[py][px]:
           continue
       for dx, dy in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
           y = py + dy
           x = px + dx
           if 0 <= y < rows and 0 <= x < cols:
               height_diff = heights[py][px] - heights[y][x]
               new_dist = dist + sqrt(step * step + height_diff * height_diff)
               if distances[y][x] > new_dist:
                   parents[y][x] = (py, px)
                   distances[y][x] = new_dist
                   heapq.heappush(heap, [new_dist, (y, x)])
```
* Поки всі вершини не розглянуті, ми беремо з heap координату із найкоротшою відстанню до початкової
* Якщо це кінцева вершина, то закінчуємо ітерацію
* Якщо вже був знайдений шлях коротший, за той, що пропонується, то одразу переходимо на нову ітерацію циклу
* Ітеруємо всі координати вершин, які суміжні з даною, і рахуємо нову довжину шляху для них. Якщо до сусідньої вершини не було знайдено шляху коротшого, то оновлюємо його та масив parents і додаємо в heap вершину на розгляд.
### Backtracking (пошук з поверненням)
```python:core/dijkstra.py [45-48]
path = [point2]
while path[-1] != point1:
    path.append(parents[path[-1][0]][path[-1][1]])
return distances[point2[0]][point2[1]], path[::-1]
```
* Нехай у масиві path буде зберігатися шлях із кінцевої вершини в початкову, тоді напочатку path має один елемент: кінцеву вершину
* На кожній ітерації, поки в шлях не буде додана початкова вершина, будемо додавати в path вершину з якої ми прийшли в останній елемент path
* Після завершення ітерації повертаємо кортеж із самої довжини шляху та масив координат шляху
### Оцінка складності алгоритму
* Оскільки ми розглядаємо максимум n вершин і для кожної з них виконуємо операції додати в heap і виняти з heap, складність яких O(log(n)), то загальна складність алгоритму O(nlog(n)). Реальний час роботи буде представлений згодом
### Команда для запуску алгоритму Dijkstra для тесту test.txt і запису результату у файл result.txt
```
python3.9 core/finder.py tests/test.txt results/result.txt --dijkstra
```
## Модуль A*
### Навіщо два алгоритми?
* Оскільки вхідні дані, скоріше за все не можуть бути будь-якими, а явлються собою поверхню (surface), то маємо саме той випадок, коли краще застосувати модифікацію Dijkstra - алгоритм A\*.
### В чому різниця?
* Якщо в алгоритмі Dijkstra з heap ми брали вершину з найменшою відстанню до початкової, то A\* бере модифіковану дистанцію, яка є сумою найкоротшої відстані до початкової вершини та евристичної дистанції h(x).
### h(x)
* Це евристична функція, яка оцінює знизу вартість шляху від вершини x до кінцевої. Оскільки важливо, щоб h(x) була не більша ніж реальний шлях до кінцевої вершини, то h(x) рахуємо як step * manhattan_distance(x, E), де E - кінцева вершина. Можна було б врахувати різницю висот, але, оскільки вона зазвичай мала в порівнянні із манхеттенською відстанню і операція взведення в степінь та корінь є достатньо не швидка, то особливо немає сенсу це робити.
### Зміни в реалізації
```python:core/a_star.py
hdistances = [[inf for _ in range(cols)] for _ in range(rows)]
hdistances[point1[0]][point1[1]] = step * manhattan_distance(point1, point2)
```
* Тепер будемо крім масиву distances, зберігати hdistances[y][x] - найкоротшу довжину шляху від початкової вершини до (y, x) + оцінену(мінімальну) відстань від (y, x) до кінцевої.
```python:core/a_star.py
if distances[y][x] > new_dist:
    parents[y][x] = (py, px)
    distances[y][x] = new_dist
    new_dist += step * manhattan_distance(point2, (y, x))
    hdistances[y][x] = new_dist
    heapq.heappush(heap, [new_dist, (y,x)])
```
* В heap теж будемо додавати суму реальної та оціненої відстані, проте в distances[y, x] зберігатимемо ту саму найкоротшу довжину шляху від початкової вершини до (y, x)
### Команда для запуску алгоритму A* для тесту test.txt і запису результату у файл result.txt
```
python3.9 core/finder.py tests/test.txt results/result.txt
```
## Порівняння алгоритмів A* та Dijkstra
### Порівняння на тестах, де потрібно йти з лівого верхнього кута мапи в правий нижній (логарифмічна шкала):
![Comparison](./assets/comparison.png)
Можемо бачити, що при малій кількості вершин час роботи приблизно однаковий, а от при 5000x5000 (25*10^6) A\* працює приблизно в 5 разів швидше за Dijkstra
### Порівняння на тестах, де потрібно йти з (size / 3, size / 3) в (size * 2 / 3, size * 2 / 3):
![Comparison](./assets/comparison2.png)
Можемо бачити, що тепер алгоритм A* в рази швидше за Dijkstra. Наприклад, для 25M вершин A* працює 45 секунд, а Dijkstra 429 секунд.

## Features
### Використання на реальних даних
* Щоб запустити алгоритм на даних певної поверхні, яка не задана в текстовому файлі, був розроблений модуль H2T (Heightmap to test), який зчитує чорно-білу карту висот та генерує текстовий тест. Зразок такої карти:
![Heighmap](./assets/map1.png)
* Зручність полягає у тому, що таку карту можна як згенерувати в певній програмі, так і взяти з реальної поверхні Землі, використовуючи https://tangrams.github.io/heightmapper/

Команда для запуску H2T:
```
python3.9 utils/h2t.py heightmaps/heightmap.png tests/test.txt start_row start_col end_row end_col --min_height --max_height
```
### Візуалізація
* Для інтерактивного відображення накоротшого шляху на поверхні розроблений модуль visualizer:
![Heighmap](./assets/map3d.png)

Команда для візуалізації:
```
python3.9 utils/visualizer.py tests/test.txt results/result.txt
```

## Розподіл роботи
* Пошук шляху за алгоритмом Dijkstra — Омельчук Олег, Плетінка Андрій
* Пошук шляху за алгоритмом A* — Митник Олексій
* Порівняння алгоритму Dijkstra і A* — Митник Олексій 
* H2T — Мазурик Антон
* Візуалізатор — Іванов Сергій
* Unit Тести — Мазурик Антон, Плетінка Андрій
