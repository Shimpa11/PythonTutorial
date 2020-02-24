import numpy as np
a1=np.arange(10,21)
print(a1)
a2=np.array(list(range(10,21)))
print(a2)

# with step
a3=np.arange(10,21,3)
print(a3)

# a4=np.ones(3,3,3)
a4=np.ones((3,3,3),dtype=np.int)

print(a4)
# linear spacing

# dividing images into number of parts
a5=np.linspace(0,21,4)
print(a5)