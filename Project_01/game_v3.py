"""The computer guesses the number and guesses the number by itself.
    And it does it in less than 20 tries.
"""
import numpy as np

np.random.seed(1)
number = np.random.randint(1,101)

def random_predict(number:int=1) -> int:
    """Guessing a random number

    Args:
        number (int): _description_. Defaults to 1.

    Returns:
        int: _description_
    """

print(number)