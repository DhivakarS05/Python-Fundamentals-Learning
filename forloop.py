#####################for loop practice##################
#print 1-10
for i in range(1,11):
    print(i,end=" ")

#print Char
fruit = "APPLE"
for i in fruit:
    print(i,end=" ")

#nested for loop
for i in range(2,3):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

#mini project for multiplication table
num = int(input("Enter a number to be multiple: "))
for i in range(1,11):
    print(f"{num}*{i}={num*i}")

#print each letter in your name
Name = input("Enter Your Name: ")
for i in Name:
    print(i,end=" ")

#print square of number from 1-5
for i in range(1,6):
    print(i**2)

#print all elements in a list of your favorite movie
movies = ["Leo","Goat","Master","Jananayagan","Sarkar","Bigil"]
for i in movies:
    print(i,end=" ")

#print sum of n numbers
n = int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum = sum + i
print(sum)

#count digit in a number
n = input("Enter a number: ")
count = 0
for i in n:
    count = count+1
print(count)


#reverse print
for i in range(10,0,-1):
    print(i,end=" ")

#factorial program
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)

#sum of digit
n = int(input())
sum = 0
for i in str(n):
    sum = sum +int(i)
print(sum)

#print vowels
name = input()
count = 0
for i in name:
    if i in "a,e,i,o,u":
        count = count+1
print(count)


#prime numbers
n = int(input())
for i in range(2,n):
    if n % i == 0:
        print("not prime")
        break
    else:
        print("prime")
        break
#pattern program
n = 5
for i in range(1,n+1):
    print("*"*i)

#fibonacci
n = 7
a,b=0,1
for i in range(n):
        print(a,end=" ")
        a,b=b,a+b


#reverse a string
s = input("Enter string: ")
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
