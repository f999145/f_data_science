import numpy as np

workers = ['Ivan', 'Nikita', 'Maria', 'John', 'Kate']
 
choice = np.random.choice(workers, size=(2,2), replace=False)
print(choice)
table = np.random.randint(1, 101, (3,2), np.uint8)
print(np.info(table))