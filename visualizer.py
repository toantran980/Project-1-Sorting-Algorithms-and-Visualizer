import pygame
import random
import time 

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
# Colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Draw each array
def draw_array(screen, arr, title, highlight_index=None):
    screen.fill(BLACK)
    bar_width = WIDTH // len(arr) if len(arr) > 0 else 1
    max_height = max(arr) if arr else 1

    # Draw title
    font = pygame.font.Font(None, 36)
    text = font.render(title, True, RED)
    screen.blit(text, (10, 10))

    for i in range(len(arr)):
        bar_height = (arr[i] / max_height) * (HEIGHT - 50)
        color = GREEN if i == highlight_index else BLUE
        pygame.draw.rect(screen, color, (i * (bar_width + 2), HEIGHT - bar_height, bar_width, bar_height))

    pygame.display.update()

# Bubble Sort Visualization
def bubble_sort_visual(arr):
    n = len(arr)
    steps = []
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append((arr.copy(), j + 1))  # Capture step with current index
    return steps

# Merge Sort Visualization
def merge_sort_visual(arr):
    steps = []
    
    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    def merge(arr, left, mid, right):
        left_half = arr[left:mid + 1]
        right_half = arr[mid + 1:right + 1]
        
        i = j = 0
        k = left
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
            steps.append((arr.copy(), k))  # Capture step with current index
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            steps.append((arr.copy(), k))  # Capture step with current index
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            steps.append((arr.copy(), k))  # Capture step with current index
    
    merge_sort_helper(arr, 0, len(arr) - 1)
    return steps

# Quick Sort Visualization
def quick_sort_visual(arr):
    steps = []

    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append((arr.copy(), j))  # Capture step with current index
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append((arr.copy(), i + 1))  # Capture step with current index
        return i + 1

    quick_sort_helper(arr, 0, len(arr) - 1)
    steps.append((arr.copy(), -1))  # Final step with no highlight
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
            steps.append((arr.copy(), i))  # Capture step with current index

    if arr:
        max_num = max(arr)
        exp = 1

        while max_num // exp > 0:
            counting_sort(arr, exp)
            exp *= 10

    steps.append((arr.copy(), -1))  # Final step with no highlight
    return steps

# Linear Search Visualization
def linear_search_visual(arr, target):
    steps = []
    for i in range(len(arr)):
        steps.append((arr.copy(), i))
        if arr[i] == target:
            return steps, i
    return steps, -1

# Visualize Sorting
def visualize_sorting(screen, sorting_function, arr, title, delay):
    steps = sorting_function(arr.copy())
    sorted_arr = steps[-1][0]
    for step, highlight_index in steps:
        draw_array(screen, step, title, highlight_index=highlight_index)
        pygame.time.delay(delay)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit immediately
    # Redraw the array with all bars in blue after sorting is complete
    draw_array(screen, sorted_arr, title)
    pygame.display.update()

# Visualize Linear Search
def visualize_linear_search(screen, arr, target):
    steps, found_index = linear_search_visual(arr, target)
    for arr_state, index in steps:
        draw_array(screen, arr_state, "Linear Search", highlight_index=index)
        pygame.time.delay(200)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return  # Exit immediately

# Main function
def visualize(screen, algo_list, arr, target):
    for algo in algo_list:
        start_time = time.time()  # Start time measurement
        if algo in ["b", "m", "q", "r"]:
            title_map = {
                "b": "Bubble Sort",
                "m": "Merge Sort",
                "q": "Quick Sort",
                "r": "Radix Sort",
            }
            delay_map = {
                "b": 5,  # delay for bubble sort
                "m": 200,  # delay for merge sort
                "q": 200,  # delay for quick sort
                "r": 200,  # delay for radix sort
            }
            visualize_sorting(
                screen,
                {
                    "b": bubble_sort_visual,
                    "m": merge_sort_visual,
                    "q": quick_sort_visual,
                    "r": radix_sort_visual,
                }[algo], arr, title_map[algo], delay_map[algo]
            )
        elif algo == "l" and target is not None:
            visualize_linear_search(screen, arr, target)

        # Brief pause before the next visualization
        pygame.time.delay(1000)  # 1 second delay before the next algorithm

        end_time = time.time()  # End time measurement
        time_nanoseconds = (end_time - start_time) * 1_000_000_000
    return time_nanoseconds

# Running it/testing
if __name__ == "__main__":
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sorting Algorithm Visualization")
    
    arr = [random.randint(0, 9999) for _ in range(5000)] # Adjusted for scalability
    target = arr[random.randint(0, len(arr) - 1)] if arr else None
    visualize(screen, ["m"], arr=arr, target=target)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
