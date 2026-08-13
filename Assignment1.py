# Assignment 1.1

for i in range(3):
    print("Lakshay Kapur")


# Assignment 2.1

a=10
b=20
c=30
print(a+b+c)


# Assignment 2.2

a="Hello"
b=" "
c="World"
print(a+b+c)


# Assignment 4.1

print("Table of 7")
for i in range(1,11):
    print(7,"*",i,"=",7*i)

print("Table of 9")
for i in range(1,11):
    print(9,"*",i,"=",9*i)


# Assignment 4.2

n=int(input("Enter n: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)


# Assignment 4.3

n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    s+=i
print(s)


# Assignment 5.1

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print(max(a,b,c))


# Assignment 5.2

n=int(input("Enter n: "))
s=0
for i in range(1,n+1):
    if i%7==0 and i%9==0:
        s+=i
print(s)


# Assignment 5.3

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


# Assignment 6.1

def addOdd(n):
    s=0
    for i in range(1,n+1):
        if i%2!=0:
            s+=i
    return s

n=int(input("Enter n: "))
print(addOdd(n))


# Assignment 6.2

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
