
#PROG 1A- Addition of two nested lists

l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=[[9,8,7],[6,5,4],[3,2,1]] 
l3=[] 
for i in range (0,len(l1)):
    temp=[]
    for j in range(0,len(l1[i])): 
        temp.append(l1[i][j]+l2[i][j]) 
    l3.append(temp)
print(l3)