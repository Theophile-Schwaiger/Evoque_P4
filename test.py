import numpy as np

F = np.zeros((4,4))
F2 = np.zeros(16,dtype = 'float')

print(F2)
F2 = np.reshape(F2,(-1,4))
print(F2)
for i in range(len(F)):
    for j in range(len(F)):
        if i == j:
            F[i,j] = 1

R = np.array([1,2,3])  
print(R[1:])      
print(F)
print(F[1:,1:])
print(F[1:,1:]@R)
