'''#different operation of string
nm = 'DEEPTI'                           #it is a string containing some value
#nm =  'D , E , E , P , T , I'          #also a string can be written like this
#nm[1] = 'i'                             #not working
print(nm)                       
print(nm[0])                            #print the value of  given index
print(nm[-1])                           #python have negative indexing also, index[-1] means last value
print(nm[1:5])                          #print the value from start  to end-1 location
print(nm[1:])                             #print the values of start location to end location
for i in nm:                            #print the string values one by one by using for loop
    print(i)

n = len(nm)                             # it returns the length of the string
i=0
while i < n :                           #print the string values one by one by using while loop
    print(nm[i])
    i+=1
j = 1
while j < n+1 :                     #print the string values reverse by negative indexing
    print(nm[-j])
    j+=1

print(type(nm))                           #print the data type 
print("E" in nm)                        #use of in operator,it returns true/false
print("A" in nm)    
print("A" not in nm)                    #use of not in operator,it returns true/false
print("hi \t python")                    #\t means tab 
print(" hi \n python")                      #\n go to next line
num = 1,2,3,4
print(type(num))
print("my name is %s and my age is %d" %('deepti' , 33))
D = nm.count(nm[0])                         # count the presence of a letter in a word
E = nm.count('E')
P = nm.count('P')
T = nm.count('T')
I = nm.count('I')
print("the letter D present in Deepti is " , nm.count('D'))            #we can write as it for count the presence of a letter in a word
print("the letter E present in Deepti is " , E)
print("the letter P present in Deepti is " , P)
print("the letter T present in Deepti is " , T)
print("the letter I present in Deepti is " , I)
print('\nthe letter %s present in DEEPTI is %d'  %('D' ,D))             #we can print as this
print('the letter %s present in DEEPTI is %d'  %('E' ,E))
str="hi i am learning python "
print(len(str))                             #it will return the length of string
print(str.count('n'))                       #it will count how many times the letter is there in string
print(str.find('i'))                        #it returns the location of the first matching letter
print(str.rfind('i'))                       #it returns the location of the last matching letter/start searching from right side
#print(str.find_all('i'))                #not working
print(str.find('z'))                        #returns the location as -1 if the letter not found
print(str.lower())                          #it returns the sentence in lower case 
print(str.upper())                          #it returns the sentence in upper case
print(str.capitalize())                     #it prints the sentence with first letter capital
print(nm)                               #it return as it is with all blank spaces
print(nm.rstrip())                      #it returns by trimming all the blank spaces which are right side of letter/sentence
print(nm.lstrip())                      #it returns by trimming/eliminating all the blank spaces which are left side of letter/sentence
for i in str:
 print (i)

print(max(str))                        #it returns the last albhabetically letter found in string
print(min(str))                        #it returns the first alphabetical letter found in string
print(str.replace('hi' , 'hello'))          #it replace a word with another word in a string
print(str.split('am'))                      #it removes the word/all the words from the string and print 
#removes all duplicate and print number of occurance
st = input("The string is : ")                      #enter a string dynamically        
s=set(st)                                       #it removes all duplicates and its data type is set
print(s)
ss="".join(s)                                    #it will show values as a string
print(ss)                                  
for i in ss:                                      
 print("the letter %s present %d times" %( i, st.count(i))) 
#find greater number using if and elif
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))
if a<0 or b<0 or c<0:
    print("you entered a negative number")
elif a>b and a>c :
    print("%d is greater" %a)
elif b>c :
    print("%d is greater" %b)
else :
    print("%d is greater" %c)

#calculate percentage and division  
tot = int(input("enter your total mark: "))
mark = int(input("enter your secured mark:  "))
per = mark*100/tot
if per >= 70 :
    print("1st division")
elif 50<=per<70:
    print("2nd division")
elif 30<=per<50:
    print("3rd division")
else:
    print("FAIL")
#use of break and continue statement in loop
subject = "c++" , "java" , "python" , "c#" , "ruby" , "python"
for i in subject:                                                           
    if i == 'python':
        print("yes got it")
        continue                                                       #here it find all matchings as it continue till searching all values
studname = "a" , "b" , "c" , "d" , "e" , "f", "c"
for i in range(len(studname)):                                        #it is using range function and indexing
    if studname[i]=='c':
        print("found it,now stop loop" , "\n The student name is " , studname[i])
        break                                                        #if it find one true statement the loop break cant search for any reapeated value
#different operation of a list
list = ["a" , "b" , "c" , "d" , "e" , "f", "c"]
print(list[:])   
list.append(2*3)                             
list = (list + [1 , "h"])                                              #add value to list
list.append('p')                                                  #append means add the value in last index
print(len(list))
list[6] = 'g'                                                       #changing a value in a particular index
print(list)
for i in range(len(list)) :                                       #here we can read all value of list 
  print(list[i:i+1:len(list)])                                       #use of for...else... loop
else:
    print("list is over") 

#use of function
def nname():
    print("it is a function call")                          
nname()                                                             #function call without argument
def sum(a,b):
    print(a+b)
sum(2,6)                                                           #function call with two argument
def mul(a):
    print("multiply with 10 will be " , a*10)
mul(7)                                                              #function call with one argument
#we can define and call a function in differnt way
def nname1(name):
    print(name)                         
nname1("deepti")                                                   #function define and call with one argument

#If we call the function without argument, it uses the default value
def name2(name = "deepti"):
    print('my name is ', name)
name2('ishi')                                                   
name2('iti')
name2()                                                         #function define  with default parameter
name2('aadya')                                                          
#function with 2 argument
def my_func1(fname, lname):
  print(fname + " " + lname)
my_func1("deep", "pat")
my_func1('ishi' , 'iti')
#we can also send arguments with the key = value syntax
def my_func2(child3, child2, child1):
  print("The youngest child is " + child3)
my_func2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#If the number of arguments is unknown, add a * before the parameter name:
def my_func3(*kids):
  print("The youngest child is " + kids[2])
my_func3("Emil", "Tobias", "Linus")
# having an empty function definition like this, would raise an error without the pass statement
def myfunction():
  pass
#pass a list into a function
def sub(list):
    print(list[2])
    print(list[::2])
    for x in list:
        print(x)
#subnam = ['python','java','ruby','api','jira','selenium']
sub(['python','java','ruby','api','jira','selenium'])
#function call with return
def add(a,b):
    c=a+b
    return c
x = add(4,7)                                                #function call with return
print(x)
#if elif loop within a function
def launchbrowser(browser):
    if browser=='chrome':
        return "chrome browser launching"
    elif browser=='firefox':
        return 'firefox is launching'
    elif browser=='internetexplorer':
        return 'IE is launching'
    else:
        return 'unknown browser'
print(launchbrowser('chrome'))
print(launchbrowser('edge'))
print(launchbrowser('internetexplorer'))
print(launchbrowser('firefox'))

#recursion function
def fact(num):
    if(num>1):
        num=num*fact(num-1)
    return num
print(fact(4))

#Lambda functions can take any number of arguments:
a = lambda a,b,c:a+b+c
print(a(2,3,4))
#a function definition that takes one argument, and that argument will be multiplied with an unknown number
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))'''

#use of function defination which can double or triple of a value
def myfunc1(n):
  return lambda a : a * n
mydoubler = myfunc1(2)
mytripler = myfunc1(3)
print(mydoubler(11)) 
print(mytripler(11))
## use of class/object
class myclass:
    x=5
    y=3
print(myclass)
c1 = myclass()
print(c1.y)
print(c1.x)
#All classes have a builtin function called __init__(), which is always executed when the class is being initiated.
class Person:                                
    student = 10                        #the variable declare inside a class is called class variable
    def __init__(self, name, age):          #it is declaration of constructor of Person class
        self.name = name                
        self.age = age                   #the variable declare inside a method are known as instance variable
p1 = Person("John", 36)                 #creating object for Person class
print(p1.name)
print(p1.age)
# data hiding(private,public)
class myclass2:
    p=5
    __q=3                                         #it is a private data member of class myclass2
c2 = myclass2()
print(c2.p)
#print(c2.__q)                            its not the way to call the private variable
print(c2._myclass2__q)                        #access private hidden data outside of class by a tricky syntax

class teacher:
    def __init__(self, name, age):            
        self.name = name                            #instance variable
        self.age = age                              #instance variable
class student(teacher):
    def __init__(self, name, age):          
        self.name = name                            #instance variable
        self.age = age                              #instance variable

p1 = teacher("aa" , 10)
print(p1.name)
print(p1.age)


