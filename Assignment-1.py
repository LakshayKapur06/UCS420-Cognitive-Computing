# Exercise 1.1. Print your name three times.

for i in range(3):
    print("Lakshay Kapur")


# Exercise 2.1. Add three numbers and print the sum.

a=10
b=20
c=30
print(a+b+c)


# Exercise 2.2. Concatenate three strings and print the result.

a="Hello"
b=" "
c="World"
print(a+b+c)


# Exercise 4.1. Print the multiplication tables of 7 and 9 up to 10.

print("Table of 7")
for i in range(1,11):
    print(7,"*",i,"=",7*i)

print("Table of 9")
for i in range(1,11):
    print(9,"*",i,"=",9*i)


# Exercise 4.2. Read a number and print its multiplication table up to 10.

n=int(input("Enter n: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


# Exercise 4.3. Read n and print the sum of the natural numbers from 1 to n.

n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    s+=i
print(s)


# Exercise 5.1. Read three numbers and print the largest.

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print(max(a,b,c))


# Exercise 5.2. Read n and sum the numbers from 1 to n divisible by both 7 and 9.

n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    if i%7==0 and i%9==0:
        s+=i
print(s)


# Exercise 5.3. Read n and print the sum of all prime numbers up to n.

n=int(input("Enter n: "))
s=0

for i in range(2,n+1):
    prime=True
    for j in range(2,i//2+1):
        if i%j==0:
            prime=False
            break
    if prime:
        s+=i

print(s)


# Exercise 6.1. Write a function that sums the odd numbers from 1 to n.

def addOdd(n):
    s=0
    for i in range(1,n+1):
        if i%2!=0:
            s+=i
    return s

n=int(input("Enter n: "))
print(addOdd(n))


# Exercise 6.2. Write a function that sums the prime numbers up to n.

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True

def addPrime(n):
    s=0
    for i in range(2,n+1):
        if isPrime(i):
            s+=i
    return s

n=int(input("Enter n: "))
print(addPrime(n))
