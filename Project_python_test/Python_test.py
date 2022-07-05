import numpy as np
print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')

a = np.float128(-456)
print(np.finfo(a))