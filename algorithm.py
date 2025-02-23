import time
import random

#Bubble sort 
def bubble_sort(students):
    n = len(students)

    for i in range(n):
        for j in range(0, n - i -1):
            if students[j][1] > students[j+1][1]:
                students[j], students[j+1] = students[j+1], students[j]

#Insertion
def insertion_sort(cards):
    for i in range(1, len(cards)):
        key = cards[i] #the card to be placed in correct position
        j = i - 1 #index of last card in sorted position

        while j >= 0 and key < cards[j]:
            cards[j + 1] = cards[j] #shift elements to the right
            j -= 1 #move one step to the left

        cards[j + 1] = key #place key in its correct posiiton

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
