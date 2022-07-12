import numpy as np

workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
 
choice = np.random.choice(workers, size=(2,2), replace=False)
print(choice)