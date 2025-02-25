import pygame
import random

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualization")

# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Draw each array
def draw_array(arr, highlight_index=None):
    screen.fill(BLACK)
    bar_width = WIDTH // len(arr) if len(arr) > 0 else 1
    max_height = max(arr) if arr else 1

    for i in range(len(arr)):
        bar_height = (arr[i] / max_height) * (HEIGHT - 50)
        color = GREEN if i == highlight_index else BLUE
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - bar_height, bar_width, bar_height))

    pygame.display.update()

# Bubble Sort Visualization
def bubble_sort_visual(arr):
    n = len(arr)
    steps = []
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            steps.append(arr.copy())
    return steps

# Merge Sort Visualization
def merge_sort_visual(arr):
    steps = []

    def merge_sort_helper(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort_helper(left_half)
            merge_sort_helper(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

            steps.append(arr.copy())

    merge_sort_helper(arr)
    return steps

# Quick Sort Visualization
def quick_sort_visual(arr):
    steps = []

    def quick_sort_helper(arr):
        if len(arr) <= 1:
            steps.append(arr.copy())
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        sorted_arr = quick_sort_helper(left) + middle + quick_sort_helper(right)
        steps.append(sorted_arr)
        return sorted_arr

    quick_sort_helper(arr)
    return steps

# Radix Sort Visualization
def radix_sort_visual(arr):
    steps = []

    def counting_sort(arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(n):
            arr[i] = output[i]

    if arr:
        max_num = max(arr)
        exp = 1

        while max_num // exp > 0:
            counting_sort(arr, exp)
            steps.append(arr.copy())
            exp *= 10

    return steps

# Linear Search Visualization
def linear_search_visual(arr, target):
    steps = []
    for i in range(len(arr)):
        steps.append((arr.copy(), i))
        if arr[i] == target:
            return steps, i
    return steps, -1

# Visualize Sorting Algorithms
def visualize_sorting(sorting_function, arr):
    steps = sorting_function(arr.copy())
    for step in steps:
        draw_array(step)
        pygame.time.delay(50)

# Visualize Linear Search
def visualize_linear_search(arr, target):
    steps, found_index = linear_search_visual(arr, target)
    for arr_state, index in steps:
        draw_array(arr_state, highlight_index=index)
        pygame.time.delay(200)

# Main function
def main(bubble, merge, quick, radix, linear, arr, target):
    running = True
    draw_array(arr)
    
    print(f"Searching for: {target}")

    # Each algo visualization
    if bubble:
        visualize_sorting(bubble_sort_visual, arr)
    if merge:
        visualize_sorting(merge_sort_visual, arr)
    if quick:
        visualize_sorting(quick_sort_visual, arr)
    if radix:
        visualize_sorting(radix_sort_visual, arr)
    if linear and target is not None:
        visualize_linear_search(arr, target)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

# running it
if __name__ == "__main__":
    arr = [random.randint(0, 9999) for _ in range(10)]
    target = arr[random.randint(0, len(arr) - 1)] if arr else None
    main(bubble=True, merge=False, quick=True, radix=False, linear=True, arr=arr, target=target)