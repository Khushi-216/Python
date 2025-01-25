n=int(input("Enter number of students needed: "))
li=[]
for i in range (n):
    li.append([])
    name=input(f"Enter name of student : {i+1} \n")
    li[i].append(name)
    print("Enter Marks of 3 subjects")
    for j in range(3):
        marks=int(input())
        li[i].append(marks)

print("Student Data: \n",li)

average=[]
for student in li:
    avg=0
    avg =round(sum(student[1:])/(len(student[1:])),2)
    average.append((student[0],avg))    

print("The Average of their marks is: ",average)

max_avg=max(average,key=lambda x:x[1])

print("Highest average marks: ",max_avg,"\n\n")
sub1=max(li,key=lambda x:x[1])
sub2=max(li,key=lambda x:x[2])
sub3=max(li,key=lambda x:x[3])

print("Highest marks in Subject 1 are ",sub1[0]," by ",sub1[1],"\n \n")
print("Highest marks in Subject 2 are ",sub2[0]," by ",sub2[2],"\n \n")
print("Highest marks in Subject 3 are ",sub3[0]," by ",sub3[3],"\n \n")





    
