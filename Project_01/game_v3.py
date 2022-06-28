"""The computer guesses the number and guesses the number by itself.
    And it does it in less than 20 attempts.
"""
import numpy as np


def random_predict(number:int=1) -> int:
    """Guessing a random number

    Args:
        number (int): The number you're looking for. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0
    
    left_side = 1       # Denote the boundaries of the interval,
    right_side = 100    # within which we will search for the target number.
    mid_num = 0
    
    while True:
        count += 1
        
        # First, we check if the number is on 
        # the boundaries of the interval 1 - 100.
        if count == 1:
            if left_side == number:
                return (count)
            count += 1
            
            if right_side == number:
                return (count)
            count += 1
        
        
        # Find the middle of the interval.
        mid_num = (left_side + right_side)//2 
        
        # If the middle of the interval is not the target number.
        # Then we move the boundary to the middle of the interval,
        # depending on whether it is greater or less than the target number.
        if mid_num == number:
            return (count)
        elif mid_num > number:
            right_side = mid_num
        else:
            left_side = mid_num


def score_game(random_predict) -> int:
    """Calculate the average number of attempts for 1000 attempts

    Args:
        random_predict (_type_): The guessing function

    Returns:
        int: Average number of attempts
    """
    count_ls = []
    random_array = np.random.randint(1,101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    
    return (score)

if __name__ == "__main__":
    # RUN
    score = score_game(random_predict)
    print(f'Your algorithm guesses the value on average in {score} attempts')