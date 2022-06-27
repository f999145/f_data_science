"""Игра угадай число
    Компьютер сам загадывает и сам угадывает число
"""
import numpy as  np

def random_predict(number:int=1) -> int:
    """ Угадываем рамдомное число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: число попыток
    """
    count = 0
    
    while True:
        count += 1
        predic_number = np.random.randint(1,101)
        if predic_number == number:
            break
    
    return (count)

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш подход

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает значение в среднем за {score} попыток')
    return (score)

if __name__ == '__name__':
    score_game(random_predict)