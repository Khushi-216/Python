#Class is the Datatype of Object
#User Defined Datatype
'''Objects need memory, classes dont'''
#class is like a blueprint, it is a collection of variables and methods
#object is a real world entity - each has a unque characteristic and behaviour
'''
(int a)
Student s1
Student is the datatype (class) 
s1 is the var (object)
'''
#Front End - Language like java/python - designing forms etc...  - OUR FOCUS
#Back End - SQL, Excel etc
'''
Constructor is a SPECIAL member function 
-> they are called implicitly 
-> initialize values
 IN PYTHON CONSTRUCTORS ARE NOT JUST SAME NAME -> ''' #__init__() 

class Student:
    def __init__(self):
        print("Constructor is called")
    def display(self):
        print("Inside Display Method")
s1=Student()   #in C- Student s1;
s1.display()

# Whenever an object of a class is created, the system assigns memory to that object through constructor 
'''
Write a python program to add two numbers using class and object'''
class Addition:
    def __init__(self,n1,n2):
        self.a=n1
        self.b=n2
        self.add=self.a+self.b

    def display(self):
        print("addition = ",self.add)

a1=Addition(1,2)   #in C- Student s1;
a1.display()


class GreatestOf2:
    def __init__(self,a,b) :
        self.n1=a
        self.n2=b
        
    def calculate(self):
        if (self.n1>self.n2):
            self.ans=self.n1
        elif (self.n1<self.n2):
            self.ans=self.n2
        else:
            self.ans=0
            
    def display(self):
        if (self.ans==self.n1):
            print(self.n1,"IS GREATER THAN",self.n2)
        elif (self.ans==self.n2):
            print(self.n2,"IS GREATER THAN",self.n1)
        else:
            print("EQUAL HAI BHAIYA")
a1=GreatestOf2(9,9)   #in C- Student s1;
a1.calculate()
a1.display()


class Book:
    def __init__(self,title,author,price,stockquantity):
        self.T=title
        self.A=author
        self.P=price
        self.S=stockquantity
    def sell_book(self,quantity):
        if (self.S>=quantity):
            self.S-=quantity
            print("Remaining Stock= ",self.S)
        else:
            print("Out Of Stock")

    def add_stock(self,quantity):
        self.S+=quantity
        print("Final Stock= ",self.S)
        
    def display_details(self):
        print("Title: ",self.T,"\nAuthor: ",self.A,"\nPrice: ",self.P,"\nAvailable Stock: ",self.S)

Sarvika=Book("Hello","Me",150,70)
Sarvika.sell_book(10)
Sarvika.add_stock(40)
Sarvika.display_details()
 