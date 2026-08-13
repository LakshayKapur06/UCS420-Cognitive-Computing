import random

from collections import Counter

# Q1 - Lists

roll_number = "1024170060"

L = [int(d) * 10 for d in roll_number]

print("Original List:", L)

L.append(55)

print("After append:", L)  # Added at end

L.insert(3, 99)

print("After insert:", L)  # Added at index 3

L.remove(55)

print("After remove:", L)  # Removed value 55

x = L.pop(3)

print("After pop:", L)

print("Popped element:", x)

L.sort()

print("Ascending:", L)

L.sort(reverse=True)

print("Descending:", L)

print("First 3:", L[:3])

print("Last 3:", L[-3:])

avg = sum(L) / len(L)

new_list = [i for i in L if i > avg]

print("Average:", avg)

print("Greater than average:", new_list)

# Q2 - Tuples

scores = tuple(L[:8])

print("\nTuple:", scores)

print("Highest:", max(scores))

print("Highest Index:", scores.index(max(scores)))

print("Lowest:", min(scores))

print("Lowest Count:", scores.count(min(scores)))

# Tuples are immutable, so they cannot be changed.

rev = list(reversed(scores))

print("Reversed as list:", rev)

value = int(input("Enter a score: "))

if value in scores:

    print("Index:", scores.index(value))

else:

    print("Not present")

try:

    scores[0] = 100

except TypeError as e:

    print("Error:", e)

# Lists can be modified but tuples cannot.

first, second, *remaining = scores

print("First:", first)

print("Second:", second)

print("Remaining:", remaining)

# Q3 - Random Numbers

random.seed(1024170060)

nums = [random.randint(100, 900) for _ in range(100)]

print("\nRandom List:")

print(nums)

odd = [i for i in nums if i % 2 != 0]

even = [i for i in nums if i % 2 == 0]

print("Odd Count:", len(odd))

print("Even Count:", len(even))

def is_prime(n):

    if n < 2:

        return False

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            return False

    return True

primes = [i for i in nums if is_prime(i)]

print("Prime Count:", len(primes))

print("Prime Numbers:", primes)

count = Counter(nums)

most = count.most_common(1)[0]

print("Most Frequent:", most[0])

print("Frequency:", most[1])

# Q4 - Sets

digits = [int(d) for d in roll_number]

A = {d * 7 for d in digits}

B = {d * 9 for d in digits}

print("\nSet A:", A)

print("Set B:", B)

print("Union:", A.union(B))

print("Intersection:", A.intersection(B))

print("A-B:", A.difference(B))

print("B-A:", B.difference(A))

# Difference gives unique elements from one set only.

# Symmetric difference gives unique elements from both sets.

print("Symmetric Difference:", A.symmetric_difference(B))

print("A subset of B:", A.issubset(B))

print("B superset of A:", B.issuperset(A))

x = int(input("Enter value to discard from A: "))

A.discard(x)

print("Updated A:", A)

# discard() does not give an error if the element is absent.

# Q5 - Dictionaries

my_dict = {

    "name": "Lakshay",

    "roll_no": "1024170060",

    "branch": "COPC",

    "age": 20,

    "city": "Faridabad"

}

my_dict["location"] = my_dict.pop("city")

print("\nAfter renaming city:", my_dict)

my_dict["cgpa"] = 9.60

print("After adding cgpa:", my_dict)

my_dict["age"] += 1

print("After updating age:", my_dict)

d1 = my_dict.copy()

d2 = my_dict.copy()

print("Pop:", d1.pop("branch"))

print(d1)

del d2["branch"]

print("After del:", d2)

# pop() returns the removed value, while del only deletes it.

print("\nDictionary Items:")

for key, value in my_dict.items():

    print(key, "->", value)

if "email" in my_dict:

    print(my_dict["email"])

else:

    print("Email key not found.")

friend_dict = {

    "name": "Karanvir",

    "roll_no": "1024060178",

    "branch": "ECE",

    "age": 20,

    "city": "Jalandhar"

}

merged = {**my_dict, **friend_dict}

print("\nMerged Dictionary:")

print(merged)

# Values from the second dictionary overwrite common keys.

string_dict = {k: v for k, v in my_dict.items() if isinstance(v, str)}

print("Only String Values:")

print(string_dict)
