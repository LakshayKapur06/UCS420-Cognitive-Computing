"""
UCS420: Cognitive Computing
Assignment-2 (List, Tuples, Set and Dictionary)
Student Name: Lakshay Kapur
Roll Number: 1024170060
"""

import random

# ==============================================================================
# 1. Create a List L that is defined as= [10, 20, 30, 40, 50, 60, 70, 80].
#    i. WAP to add 200 and 300 to L.
#    ii. WAP to remove 10 and 30 from L.
#    iii. WAP to sort L in ascending order.
#    iv. WAP to sort L in descending order.
# ==============================================================================

L = [10, 20, 30, 40, 50, 60, 70, 80]
print("Original List L:", L)

# i. Add 200 and 300 to L
L.append(200)
L.append(300)
print("i. After adding 200 and 300:", L)

# ii. Remove 10 and 30 from L
L.remove(10)
L.remove(30)
print("ii. After removing 10 and 30:", L)

# iii. Sort L in ascending order
L.sort()
print("iii. Sorted in ascending order:", L)

# iv. Sort L in descending order
L.sort(reverse=True)
print("iv. Sorted in descending order:", L)


# ==============================================================================
# 2. Create a tuple of marks scored as scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
#    and perform the following operations using tuple functions:
#    i. Identify the highest score and its index in the tuple.
#    ii. Find the lowest score and count how many times it appears.
#    iii. Reverse the tuple and return it as a list.
#    iv. Check if a specific score '76' (input by the user) is present in the tuple
#        and print its first occurrence index, or a message saying it's not present.
# ==============================================================================

scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
print("\nScores tuple:", scores)

# i. Identify highest score and index
highest = max(scores)
highest_idx = scores.index(highest)
print(f"i. Highest score: {highest} at index: {highest_idx}")

# ii. Find lowest score and count
lowest = min(scores)
lowest_count = scores.count(lowest)
print(f"ii. Lowest score: {lowest} (appears {lowest_count} times)")

# iii. Reverse tuple and return as list
reversed_scores_list = list(reversed(scores))
print("iii. Reversed tuple as list:", reversed_scores_list)

# iv. Check if score '76' is present
search_score = 76
if search_score in scores:
    print(f"iv. Score '{search_score}' is present at index: {scores.index(search_score)}")
else:
    print(f"iv. Score '{search_score}' is not present in the tuple.")


# ==============================================================================
# 3. WAP to create a list of 100 random numbers between 100 and 900. Count and print:
#    i. All odd numbers
#    ii. All even numbers
#    iii. All prime numbers
# ==============================================================================

random.seed(1024170060)
nums = [random.randint(100, 900) for _ in range(100)]
print("\nGenerated 100 random numbers between 100 and 900:")
print(nums)

# i. All odd numbers
odd_nums = [n for n in nums if n % 2 != 0]
print(f"\ni. Odd numbers count: {len(odd_nums)}")
print("Odd numbers list:", odd_nums)

# ii. All even numbers
even_nums = [n for n in nums if n % 2 == 0]
print(f"\nii. Even numbers count: {len(even_nums)}")
print("Even numbers list:", even_nums)

# iii. All prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_nums = [n for n in nums if is_prime(n)]
print(f"\niii. Prime numbers count: {len(prime_nums)}")
print("Prime numbers list:", prime_nums)


# ==============================================================================
# 4. Consider the following two sets, A and B, representing scores of two teams:
#    A = {34, 56, 78, 90} and B = {78, 45, 90, 23}
#    WAP to perform the following operations using set functions:
#    i. Find the unique scores achieved by both teams (union of sets).
#    ii. Identify the scores that are common to both teams (intersection of sets).
#    iii. Find the scores that are exclusive to each team (symmetric difference).
#    iv. Check if scores of team A are a subset of team B, and if team B is superset.
#    v. Remove a specific score X (input by the user) from set A if it exists.
# ==============================================================================

A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
print("\nTeam A scores:", A)
print("Team B scores:", B)

# i. Unique scores achieved by both teams (union)
union_scores = A.union(B)
print("\ni. Unique scores (Union):", union_scores)

# ii. Scores common to both teams (intersection)
common_scores = A.intersection(B)
print("ii. Common scores (Intersection):", common_scores)

# iii. Scores exclusive to each team (symmetric difference)
exclusive_scores = A.symmetric_difference(B)
print("iii. Exclusive scores (Symmetric Difference):", exclusive_scores)

# iv. Check subset and superset relations
print(f"iv. Is Team A a subset of Team B? {A.issubset(B)}")
print(f"    Are scores of Team B a superset of Team A? {B.issuperset(A)}")

# v. Remove specific score X from set A
score_X = 34
if score_X in A:
    A.remove(score_X)
    print(f"v. Score {score_X} removed from Set A. Updated Set A: {A}")
else:
    print(f"v. Score {score_X} is not present in Set A.")


# ==============================================================================
# 5. Write a program to rename a key city to a location in the following dictionary:
#    Given:
#    sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
#    Expected output:
#    {'name': 'Kelly', 'age': 25, 'salary': 8000, 'location': 'New york'}
# ==============================================================================

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
print("\nGiven dictionary:", sample_dict)

# Rename key 'city' to 'location'
sample_dict["location"] = sample_dict.pop("city")

print("Expected output dictionary:")
print(sample_dict)
