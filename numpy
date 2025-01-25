import numpy as np

kl = [[1,2,3],[4,5,6],[7,8,9]] 
karray = np.array(kl)
print(karray)

print(np.sum(karray))# will add all the values

print(np.sum(karray,axis=0))#axis=1 - row wise, axis = 0, column wise 

'''
1 2 3
4 5 6 
7 8 9
Subaraays'''
karray[0:3,1]
# 2 5 8
karray[0:3,0:1]
# 1
# 4
# 7
karray[1:,2:]
# 6
# 9
karray[0::2,0::2]
# ([1 3],
#  [7,9])
karray[2:,1:]
# ([[8,9]])
karray[2,1:]
#([8,9])

print(karray[karray%2==0])
# ([2,4,6,8])
'''array([[False, True, False]'
          [True, False, True]
          [False, True, False]])'''

