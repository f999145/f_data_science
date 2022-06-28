"""The computer guesses the number and guesses the number by itself.
    And it does it in less than 20 tries.
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Guessing a random number

    Args:
        number (int): The number you've riddled. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0
    
    left_side = 1
    right_side = 100
    mid_num = 0
    
    while True:
        count += 1
        
        if count == 1:
            if left_side == number:
                return (count)
            count += 1
            
            if right_side == number:
                return (count)
            count += 1
        
        mid_num = (left_side + right_side)//2
        
        if mid_num == number:
            return (count)
        elif mid_num > number:
            right_side = mid_num
        else:
            left_side = mid_num

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш подход

    Args:
        random_predict (_type_): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed()
    random_array = np.random.randint(1,101, size=(1000))
    print(random_array)
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    return (score)


score = score_game(random_predict)
print(f'Ваш алгоритм угадывает значение в среднем за {score} попыток')        
