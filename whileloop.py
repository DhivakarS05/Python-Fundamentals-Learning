###############################while loop###################################
#Print Numbers
num = 1
temp= 1
while num <=10:
    print(num , end=" ")
    num = num + 1

#Sum of Numbers
while num <= 5:
    temp = temp + num
    num=num+1
print(temp)

#Reverse Countdown
while num >= 1:
    print(num , end=" ")
    num = num - 1

#Multiplication Table
while num <= 10:
    temp = num * 5
    print(f"5 * {num} = {temp}")
    num = num + 1

#Digit Count
num = int(input("num ="))
temp=0
while num > 0:
    temp = temp + 1
    num=num//10
print(temp)

#Sum of Digits
num=456
temp = 0
while num>0:
    sum  = num % 10
    temp = temp + sum
    num = num // 10
print(temp)

#palindrome
num = 1331
temp = num
rev = 0
while num>0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10
if rev==temp:
    print("palindrome")
else:
    print("Not")

#Reverse a number
num = 1234
while num > 0:
    temp = num % 10
    num = num // 10
    print(temp, end="")

#Check Armstrong Number
num = 153
temp=num
ams=0
while num>0:
    rev = num % 10
    ams = ams + rev ** 3
    num = num // 10
if ams == temp:
    print("Armstrong number")
else:
    print("not")

#Sum of Even Digits
num=123456789
sum = 0
while num>0:
    temp = num % 10
    num = num // 10
    if temp % 2 == 0:
        sum = sum + temp
print(sum)

#Count Even and Odd Digits
num = 123456
odd = 0
even = 0
while num>0:
    temp = num % 10
    if temp % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    num = num // 10
print(f"odd={odd}")
print(f"even={even}")

#Largest Digit in a Number
num = 123456
large = 0
while num > 0:
    temp = num % 10
    if temp > large:
        large = temp
    num = num // 10
print(large)

#pattern program
num = 0
while num < 5:
    num = num + 1
    print(num * "*" * 1)

#logical operator
car = input("Enter a your fav car: or Type q to quit: ")

while not car =="q":
    print(f"my fav car is {car}")
    car = input("Enter your anthor fav car: or Type q to quit: ")
print("Bye")

#anthor logical operator
num = int(input("Enter a num: "))
while num<0 or num>10:
    print(f"{num} is not valid")
    num = int(input("Enter a num: "))
print(f"your number is {num}")