#------------------------------------------------------------
# Напоминаем способ создания словаря через список кортежей
# (ключ, значение)
if False:
    data = [('Ivan', 19),('Mark', 25),('Andrey', 23),('Maria', 20)]
    client_ages = dict(data)
    print(client_ages)

#------------------------------------------------------------
# Напишите функцию brackets(line), которая определяет,
# является ли последовательность из круглых скобок правильной.

# Посянение от себя
# В задание небыло сказано что будет текст со скобками, было сказано что столько скобки
# В итоге мы собираем стек из открытых скобок,
# и опустошаем его когда назодим закрытые скобки

if False:
    def brackets(line):
        # Напишите тело функции
        from collections import deque    
        dq = deque()
        for word in line:
            if word == "(":
                dq.append(word)
            elif word == ")":
                if not len(dq):
                    return False
                dq.pop()
        if not len(dq):
            return True
        return False

    txt = "(всем привет)"

    print(brackets(txt))

# Задание 4.4

# Что подчерпнул для себя
# Генерация списка из списка с вложенными списками.
if False:
    north_list = [elem for bill in north for elem in bill]
    # Здесь сначала цикл по списку north итератор bill
    # Потом вложенный цикл по списку bill итератор elem
    # И этот elem забивается в новый цикл.
    # То есть это свернутая форма цикла в цикле
    print(north_list)

# Напишите функцию task_manager, которая принимает список задач 
# для нескольких серверов. Каждый элемент списка состоит из кортежа 
# (<номер задачи>, <название сервера>, <высокий приоритет задачи>).

# Функция должна создавать словарь и заполнять его задачами 
# по следующему принципу: название сервера — ключ, 
# по которому хранится очередь задач для конкретного сервера. 
# Если поступает задача без высокого приоритета 
# (последний элемент кортежа — False), добавить номер задачи 
# в конец очереди. Если приоритет высокий, добавить номер в начало.

# Для словаря используйте defaultdict, для очереди — deque.

# Функция возвращает полученный словарь с задачами.

if False:
    tasks = [(36871, 'office', False),
    (40690, 'office', False),
    (35364, 'voltage', False),
    (41667, 'voltage', True),
    (33850, 'office', False)]

    def task_manager(tasks):
        from collections import defaultdict
        from collections import deque
        dict_tasks = defaultdict(deque)
        for num_task,name_s,pri_s in tasks:
            if pri_s:
                dict_tasks[name_s].appendleft(num_task)
            else:
                dict_tasks[name_s].append(num_task)
        return dict_tasks
            
    print(task_manager(tasks))

if False:
    import numpy as np

    nd_arr = np.linspace(0, 12, 12, endpoint=False).reshape(3,4)

    print(nd_arr[:2])

# Напишите функцию get_chess, которая принимает на вход длину 
# стороны квадрата a и возвращает двумерный массив формы (a, a), 
# заполненный 0 и 1 в шахматном порядке. В левом верхнем углу всегда 
# должен быть ноль.

if False:
    def get_chess(a):
        import numpy as np
        arr = np.zeros((a,a),dtype=np.uint8)
        arr[1::2,::2] = 1
        arr[::2,1::2] = 1
        return arr

    print(get_chess(4))

# Вы разрабатываете приложение для прослушивания музыки. Конечно же, 
# там будет доступна функция перемешивания плейлиста. Пользователю может 
# настолько понравиться перемешанная версия плейлиста, что он захочет 
# сохранить его копию. Однако вы не хотите хранить в памяти новую версию 
# плейлиста, а просто хотите сохранять тот seed, с которым он был 
# сгенерирован.

if False:
    def shuffle_seed(array):
        import numpy as np
        seed_r = np.random.randint(2**32, dtype=np.uint32)
        np.random.seed(seed_r)
        return (np.random.permutation(array),seed_r)
        print(seed_r)
        
    print(shuffle_seed([1,2,3,4,5]))

# Напишите функцию min_max_dist, которая принимает на вход неограниченное 
# число векторов через запятую. Гарантируется, что все векторы, которые 
# передаются, одинаковой длины.

# Функция возвращает минимальное и максимальное расстояние между векторами 
# в виде кортежа.

# Общая формула, которая позволяет найти число 
# сочетаний из n объектов по k имеет вид:
# Ckn=n!/((n−k)!*k!).

if False:
    def min_max_dist(*vectors):
        import numpy as np
        fac_vac = np.math.factorial(len(vectors)) // (np.math.factorial(len(vectors)-2) * 2)
        fac_arr = np.zeros(fac_vac)
        ik = 0
        for ir in range (len(vectors) - 1):
            for jr in range (ir+1, len(vectors)):
                fac_arr[ik] = np.linalg.norm(vectors[ir] - vectors[jr])
                ik += 1
        return (np.amin(fac_arr),np.amax(fac_arr))
        
    import numpy as np
    vec1 = np.array([1,2,3])
    vec2 = np.array([4,5,6])
    vec3 = np.array([7,8,9])
    
    print(min_max_dist(vec1, vec2, vec3))

# Напишите функцию any_normal, которая принимает на вход неограниченное 
# число векторов через запятую. Гарантируется, что все векторы, которые 
# передаются, одинаковой длины.

# Функция возвращает True, если есть хотя бы одна пара перпендикулярных 
# векторов. Иначе возвращает False.

if False:
    def any_normal(*vectors):
        import numpy as np
        for ir in range (len(vectors) - 1):
                for jr in range (ir+1, len(vectors)):
                    if np.dot(vectors[ir], vectors[jr]) == 0:
                        return True
        return False

    import numpy as np

    vec1 = np.array([2, 1])
    vec2 = np.array([-1, 2])
    vec3 = np.array([3,4])
    print(any_normal(vec1, vec2, vec3))

# Напишите функцию get_loto(num), генерирующую трёхмерный массив случайных 
# целых чисел от 1 до 100 (включительно). Это поля для игры в лото.

# Трёхмерный массив должен состоять из таблиц чисел формы 5х5, то есть 
# итоговая форма — (num, 5, 5).

# Функция возвращает полученный массив.

if False:
    def get_loto(num):
        import numpy as np
        arr = np.random.randint(1,101,(num,5,5),np.uint8)
        return arr

    print (get_loto(3))

# Напишите функцию get_unique_loto(num). Она так же, как и функция 
# в задании 10.10, генерирует num полей для игры в лото, однако 
# теперь на каждом поле 5х5 числа не могут повторяться.

# Функция также должна возвращать массив формы num x 5 x 5.

if False:
    def get_unique_loto(num):
        import numpy as np
        arr_null = np.arange(1,101)
        arr = np.zeros((num,5,5),np.int8)
        for i in range(num):
            arr[i] = np.random.choice(arr_null,(5,5),replace=False)
        return arr

    print(get_unique_loto(3))

