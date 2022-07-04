# История обучения в Блоке 2

## Модуль 10

### Модуль Collections. Counter и defaultdict

#### Counter

```python
# Импортируем объект Counter из модуля collections
from collections import Counter
# Создаём пустой объект Counter
c = Counter()
```



*Counter сразу передать в круглых скобках итерируемый объект, в котором необходимо посчитать значения:*

```python
c = Counter(cars)
print(c)
# Counter({'red': 3, 'black': 3, 'blue': 2, 'white': 1})
```
*В этой конструкции мы сначала получаем элементы (число раз, когда встретился ключ) с помощью функции values (такая же функция есть и у словаря):*

```python
print(c.values())
# dict_values([3, 2, 3, 1])
```

*Узнать сумму всех значений в объекте Counter можно, воспользовавшись следующей конструкцией:*

```python
print(sum(c.values()))
# 9
```

*Чтобы узнать, сколько машин разных цветов встретилось в двух городах, можно сложить два исходных счётчика и получить новый счётчик:*

```python
print(counter_moscow + counter_spb)
# Counter({'black': 6, 'white': 5, 'yellow': 5, 'red': 2})
```
*Чтобы узнать разницу между объектами Counter, необходимо воспользоваться функцией subtract, которая меняет тот объект, к которому применяется.*

```python
counter_moscow.subtract(counter_spb)
print(counter_moscow)
# Counter({'black': 2, 'yellow': 1, 'white': -1, 'red': -2})

print(counter_moscow - counter_spb)
# Counter({'black': 2, 'yellow': 1})
```

*Чтобы получить список всех элементов, которые содержатся в Counter, используется функция elements(). Она возвращает итератор, поэтому, чтобы напечатать все элементы, распакуем их с помощью *:*

```python
print(*counter_moscow.elements())
# black black black black white white yellow yellow yellow
```

*Чтобы получить список уникальных элементов, достаточно воспользоваться функцией list():*

```python
print(list(counter_moscow))
# ['black', 'white', 'yellow']
```

*С помощью функции dict() можно превратить Counter в обычный словарь:*

```python
print(dict(counter_moscow))
# {'black': 4, 'white': 2, 'yellow': 3}
```

*Функция most_common() позволяет получить список из кортежей элементов в порядке убывания их встречаемости:*

```python
print(counter_moscow.most_common())
# [('black', 4), ('yellow', 3), ('white', 2)]

print(counter_moscow.most_common(2))
# [('black', 4), ('yellow', 3)]
```

#### Defaultdict


```python
from collections import defaultdict
```

### Модуль Collections. Deque и OrderedDict

#### OrderedDict

- OrderedDict - Позволяет сохранять порядок в словарях
  - Устарел начиная с pyton 3.6

```python
from collections import OrderedDict
```

#### Deque
- Deque -  более расширенный функционал списков
- Объединение понятия Очередь и Стек (стопка)

```python
from collections import deque
```
У deque есть четыре ключевые функции:
- append (добавить элемент в конец дека);
- appendleft (добавить элемент в начало дека);
- pop (удалить и вернуть элемент из конца дека);
- popleft (удалить и вернуть элемент из начала дека).
- reverse позволяет поменять порядок элементов в очереди на обратный
- rotate переносит заданных элементов из конца очереди в начало
- index позволяет найти первый индекс искомого элемента
- count позволяет подсчитать, сколько раз элемент встретился в очереди

*С помощью pop всегда удаляется последний элемент из дэка. Чтобы удалить конкретный элемент по индексу, необходимо воспользоваться встроенной конструкцией **del**:*
```python
clients = deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
print(clients)
# deque(['Ivanov', 'Petrov', 'Smirnov', 'Tikhonova'])
del clients[2]
print(clients)
# deque(['Ivanov', 'Petrov', 'Tikhonova'])
```

