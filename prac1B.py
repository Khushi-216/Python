#PRAC 1 B Multiplication table using nested list
l=[]
n=int(input("How many multiplication tables r needed? "))
for i in range(0,n):
      l.append([])
      a=int(input("Enter the number:"))
      print("Enter length of table needed for ",a )
      n2=int(input())
      for j in range (1,n2+1):
          l[i].append(a*j)
      


print(l)
