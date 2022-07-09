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

