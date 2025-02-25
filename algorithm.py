import time
import random

#Bubble sort 
def bubble_sort(students):
    n = len(students)

    for i in range(n):
        for j in range(0, n - i -1):
            if students[j][1] > students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]

#Merge
def merge_sort(flights):
    if len(flights) > 1:
        mid = len(flights) // 2 #find middle index
        left_half = flights[:mid] #divide list into halves
        right_half = flights[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] < right_half[j][1]:
                flights[k] = left_half[i]
                i += 1
            else:
                flights[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            flights[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            flights[k] = right_half[j]
            j += 1
            k += 1
#Linear
def linear_search(L, T):
    result = []
    for i in range(len(L)):
        if L[i] == T:
            result.append(i)
    return result

#Radix
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # count occurences of each digit in the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
    
    #update count[i] so that it contains actual positon in the output
    for i in range(1, 10):
        count[i] += count[i - 1] #cumulative sum for stable sorting

    #build the output array by placing elements in correct order
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1 # decrement count to handle duplicates

    #copy sorted output back to original array
    for i in range(n):
        arr[i] = output[i] #overwrite original array with sorted values

def radix_sort(arr):
    #Least significant digit approach (LSD)
    #Find the max number to determine the # of digits
    max_num = max(arr)
    exp = 1

    #continue sorting for each digit place value
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

#Quick
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Take user input for list elements
"""user_input = input("Enter a list of integers separated by spaces: ")
L = list(map(int, user_input.split()))

# Take user input for target element
T = int(input("Enter an the target element to search: "))

# Calling the linear_search function and store the result
result = linear_search(L, T)

# Display the result
if result != -1:
    print(f"Element {T} found at the index {result}.")
else:
    print(f"Element {T} not found at index {result}")
print()


num_students = int(input("Enter the number of students: "))
students = []
for _ in range(num_students):
    name = input("Enter student name: ")
    score = int(input(f"Enter {name}'s score: "))
    students.append((name, score))
bubble_sort(students)
print("Sorted students by score: ", students)


# Taking user input
num_flights = int(input("Enter number of flights: "))
flights = []
for _ in range(num_flights):
    flight_no = int(input("Enter flight number: "))
    dep_time = int(input(f"Enter departure time for {flight_no}: "))
    flights.append((flight_no, dep_time))

    merge_sort(flights)

# print the sorted flights and execution time
print("Flight sorted by departure time: ", flights)

print()

random_list = [random.randint(10, 9999) for _ in range(10)]
print("Orginal Array:", random_list)
sorted_arr = quick_sort(random_list)
print("Sorted Array:", sorted_arr)

print()

random_list = [random.randint(10, 9999) for _ in range(10)]

print("Orginal Array:", random_list)
sorted_arr = radix_sort(random_list)
print("Sorted Array:", sorted_arr)"""