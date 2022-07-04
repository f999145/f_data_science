# История обучения в Блоке 2

## Модуль 10
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

