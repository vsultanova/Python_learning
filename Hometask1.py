# 1. Create list of 100 random numbers from 0 to 1000

# import the library
import random

# create an empty list
random_list = []
# add random number one by one to the empty list
for i in range(10):
    random_list.append(random.randint(0, 10))

# show the list with random numbers
print("initial list with random numbers: ", random_list)

# 2. Sort list from min to max (without using sort())
# create a empty list for further copying to it
sorted_list = []
# create a new list from the list with random numbers
unsorted_list = random_list.copy()

# create a cycle to select min number from the copied list
for i in range(len(unsorted_list)):
    # select min number from the copied list
    m = min(unsorted_list)
    # add the min number to the new sorted list
    sorted_list.append(m)
    # remove the min number from the old unsorted list
    unsorted_list.remove(m)

# show the list with sorted numbers
print("final sorted list: ", sorted_list)

# 3. Calculate average for even and odd numbers
# create two new lists for further odd and even numbers from the random list
odd_list = []
even_list = []
# check the random numbers from the initial list to split them in to two new lists
for i in range(len(random_list)):
    if random_list[i] % 2 == 0:
        even_list.append(random_list[i])
    else:
        odd_list.append(random_list[i])

# create initial sum variable for even list
sum_even_list = 0

# create initial sum variable for odd list
sum_odd_list = 0

# calculate the sum for the even list
for i in range(len(even_list)):
    sum_even_list += even_list[i]

# calculate the sum for the odd list
for i in range(len(odd_list)):
    sum_odd_list += odd_list[i]

# 4. Print both average results in console
# calculate the average for even list
try:
    avr_even_list = sum_even_list/len(even_list)
except ZeroDivisionError:
    print("There is an empty even list")
else:
    print("The average for even list: ", avr_even_list)


# calculate the average for odd list
try:
    avr_odd_list = sum_odd_list/len(odd_list)
except ZeroDivisionError:
    print("There is an empty odd list")
else:
    print("The average for odd list: ", avr_odd_list)

# Each line of code should be commented with description.

# Commit script to git repository and provide link as home task result.
