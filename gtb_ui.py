import time
import random
import time
import tkinter as tk
from tkinter import ttk

# Initialize pygame
pygame.init()

# Set window dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sorting Algorithm Visualization')

# Colors
BACKGROUND = (0, 0, 0)  # Black background
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)  # Sorted elements
YELLOW = (255, 255, 0)  # Elements being compared
PURPLE = (128, 0, 128)  # Elements being swapped

# Set the font for text rendering
font = pygame.font.SysFont("Arial", 24)

# Sorting Algorithms (from user input)

# Bubble Sort
def bubble_sort(arr, draw_bars, clock, pause_flag):
    n = len(arr)
    for i in range(n):
        if pause_flag[0]: break
        for j in range(0, n - i - 1):
            draw_bars(arr, [YELLOW if k == j or k == j + 1 else WHITE for k in range(len(arr))])
            pygame.time.delay(10)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                draw_bars(arr, [PURPLE if k == j or k == j + 1 else WHITE for k in range(len(arr))])
                pygame.time.delay(50)
            draw_bars(arr, [WHITE if k != j and k != j + 1 else YELLOW for k in range(len(arr))])
        draw_bars(arr, [GREEN if k >= n - i - 1 else WHITE for k in range(len(arr))])
        pygame.time.delay(50)

# Insertion Sort
def insertion_sort(arr, draw_bars, clock, pause_flag):
    for i in range(1, len(arr)):
        if pause_flag[0]: break
        key = arr[i]
        j = i - 1
        draw_bars(arr, [YELLOW if k == i or k == j else WHITE for k in range(len(arr))])
        pygame.time.delay(50)
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            draw_bars(arr, [PURPLE if k == j + 1 else WHITE for k in range(len(arr))])
            pygame.time.delay(50)
        arr[j + 1] = key
        draw_bars(arr, [GREEN if k <= i else WHITE for k in range(len(arr))])
        pygame.time.delay(50)

# Merge Sort
def merge_sort(arr, draw_bars, clock, pause_flag):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort_helper(arr):
        if len(arr) <= 1: return arr
        mid = len(arr) // 2
        left = merge_sort_helper(arr[:mid])
        right = merge_sort_helper(arr[mid:])
        return merge(left, right)

    arr[:] = merge_sort_helper(arr)

# Radix Sort (Using Counting Sort as the subroutine)
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # count occurrences of each digit in the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # update count[i] so that it contains actual position in the output
    for i in range(1, 10):
        count[i] += count[i - 1]  # cumulative sum for stable sorting

    # build the output array by placing elements in correct order
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1  # decrement count to handle duplicates

    # copy sorted output back to original array
    for i in range(n):
        arr[i] = output[i]  # overwrite original array with sorted values

def radix_sort(arr, draw_bars, clock, pause_flag):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
        draw_bars(arr, [YELLOW if i < len(arr) // 2 else WHITE for i in range(len(arr))])
        pygame.time.delay(50)

# Quick Sort
def quick_sort(arr, draw_bars, clock, pause_flag):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    arr[:] = quick_sort(left, draw_bars, clock, pause_flag) + middle + quick_sort(right, draw_bars, clock, pause_flag)

# Draw bars for visualization
def draw_bars(arr, color_array):
    bar_width = width // len(arr)
    screen.fill(BACKGROUND)  # Fill background to clear previous frame
    for i in range(len(arr)):
        pygame.draw.rect(screen, color_array[i], (i * bar_width, height - arr[i], bar_width, arr[i]))
    pygame.display.update()

# Tkinter window for controls
def create_gui(start_sorting_func, pause_flag, reset_flag):
    root = tk.Tk()
    root.title('Sorting Algorithm Controller')

    label = tk.Label(root, text="Choose Sorting Algorithm", font=("Arial", 14))
    label.pack(pady=10)

    algorithms = ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Radix Sort', 'Quick Sort']
    algorithm_var = tk.StringVar()
    algorithm_var.set(algorithms[0])

    algorithm_menu = ttk.Combobox(root, textvariable=algorithm_var, values=algorithms)
    algorithm_menu.pack(pady=10)

    def start_sorting():
        algorithm = algorithm_var.get()
        array = random.sample(range(0, 10000), 200)  # Generate random list with range 0-9999
        if algorithm == 'Bubble Sort':
            start_sorting_func(bubble_sort, array)
        elif algorithm == 'Insertion Sort':
            start_sorting_func(insertion_sort, array)
        elif algorithm == 'Merge Sort':
            start_sorting_func(merge_sort, array)
        elif algorithm == 'Radix Sort':
            start_sorting_func(radix_sort, array)
        elif algorithm == 'Quick Sort':
            start_sorting_func(quick_sort, array)

    start_button = tk.Button(root, text="Start Sorting", command=start_sorting)
    start_button.pack(pady=20)

    def toggle_pause():
        pause_flag[0] = not pause_flag[0]  # Toggle the pause state

    pause_button = tk.Button(root, text="Pause", command=toggle_pause)
    pause_button.pack(pady=20)

    # Function to handle reset logic
    def reset_sorting():
        reset_flag[0] = True  # Reset flag to trigger reset

    reset_button = tk.Button(root, text="Reset", command=reset_sorting)
    reset_button.pack(pady=20)

    root.mainloop()

# Main loop to handle the sorting process
def main():
    pause_flag = [False]  # [0] is used to modify the state of pause (True for paused, False for running)
    reset_flag = [False]

    def start_sorting_func(sort_algorithm, array):
        clock = pygame.time.Clock()
        sort_algorithm(array, draw_bars, clock, pause_flag)
    
    create_gui(start_sorting_func, pause_flag, reset_flag)
    
    pygame.quit()

if __name__ == "__main__":
    main()
