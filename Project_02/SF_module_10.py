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

if False
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

