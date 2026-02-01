#List is ordered and changeable allow duplicates
#index starts at 0
#create a list

fruits = ["apple","orange","banana","grapes"]
numbers = [10,20,30,40,50]
mixed = [1.5,"cars",5,True]
print(mixed)

#access list element
print(numbers[0])
print(numbers[-1])

#update list element
numbers[1]=25
print(numbers)

#add item in list
numbers.append(60)
print(numbers)

#remove item in a list
numbers.remove(60)

#pop
numbers.pop(0)
print(numbers)

#clear
numbers.clear()

#len of list
print(len(numbers))

#loop through a list
marks = [78,98,75,89]
for m in marks:
    #print(m)

#loop with index
for i in range(len(marks)):
    print(i,marks[i])
print(len(marks))

#student mark analysis:
total = 0
for m in marks:
    total = m + total
average = total/len(marks)
print("total",total)
print("average",average)

#practice program
#list creation and print sum
mark = [78,89,76,94,72]
sum = 0
for m in mark:
    sum = m + sum
print(sum)

#max value
numbers = [10,20,30,40,50]
max = numbers[0]
for n in numbers:
    if n > max:
        max = n
print("Maximum number:",max)

#count marks
marks = [76,70,78,72,79,85,90]
count = 0
for i in marks:
    if i>75:
        count = count+1
print("Above 75 is:",count)

#replace 0
marks = [32,36,38,45,50,89]
for m in range(len(marks)):
    if marks[m]<40:
        marks[m]=0
print(marks)

#replace min mark with 0
marks = [65,86,46,96,60]
min = marks[0]
for m in marks:
    if m<min:
        min=m
index = marks.index(min)
marks[index]=0
print(marks)

#reverse a list
marks = [32,36,38,45,50,89]
for m in reversed(marks):
    print(m)

numbers = [1,2,3,4,5]
reversed_list = []
for i in range(len(numbers)-1,-1,-1):
    reversed_list.append(numbers[i])
print(reversed_list)

n=[1,2,3,4,5]
rev_list=[]
for i in range(len(n)-1,-1,-1):
    rev_list.append(n[i])
print(rev_list)



#set is unordered and immutable but add/remove ok
numbers = {1,2,3,4,5}
print(type(numbers))
duplicates = {1,1,2,3,4}
print(duplicates)

numbers.add(50)
print(numbers)
numbers.remove(50)
print(numbers)

#set operations
a={1,2,3}
b={2,3,4}
print(a|b)
print(a&b)
print(a-b)

#real example for set
visitors = ["A","B","C","A","C"]
unique_visitors=set(visitors)
print(len(unique_visitors))

#convert a list duplicates to unique
array=[1,2,2,3,4,1,5,5]
unique=set(array)
print(unique)

#check if value exists
n = {10,20,30,40,50}
num = int(input("Enter a value: "))
if num in n:
    print("already exists")
else:
    print("doesn't exists")

#find a common element
a=[1,2,3]
b=[2,3,4]
set_a = set(a)
set_b = set(b)
print(list(set(a)&set(b)))

#tuple to store a data
date = (1,"Feb",2026)
day,month,year=date
print("Date: ",day,month,year)

#swap a two tuple
a= (1,2,3,4)
b=(2,4,6,8)
a,b=b,a
print(a)
print(b)

numbers = {10,10,20,30}
print(numbers)


#tuple is order and unchangeable duplicates ok faster
marks = (20,10,40,59,60)
names = ("gopi","mahi","Gokul")
print(names)
print(marks[-1])

#tuple unpacking
a,b,c = (10,20,30)
print(a)
print(b)
print(c)
print(max(a,b,c))
print(min(a,b,c))


fruits=("apple","orange","banana","grapes")
print(fruits.index("apple"))
print(fruits[0])
print(len(fruits))
for fruit in fruits:
    print(fruit)