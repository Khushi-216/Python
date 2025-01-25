'''l=[[1,2,3],[4,5,6],[7,8,9]]
print("Original list is: ",l)
for i in range (0,len(l)):
    for j in range(0,len(l[i])):
        l[i][j]*=2

print("Modified list is: ",l)
'''

USER DEFINED NESTED LIST:
l1=[]

n = int(input("Enter the number of sublist: "))

for i in range(0,n):
    l1.append([])
    print("Enter number of values of sublist ",i+1)
    n1=int(input())
    print("Enter values of sublist ",i+1)
    for j in range(0,n1):
        k=(int(input()))
        l1[i].append(k)                


print(l1)

'''










