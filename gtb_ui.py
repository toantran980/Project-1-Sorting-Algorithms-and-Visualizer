import time
import random
import pygame

# Sorting algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

def generate_array(size, condition="random"):
    if condition == "sorted":
        return list(range(size))
    elif condition == "reversed":
        return list(range(size, 0, -1))
    else:  # Random case
        return [random.randint(0, 10000) for _ in range(size)]

# Measure execution times
sizes = [100, 500, 1000, 2000, 5000]
conditions = ["random", "sorted", "reversed"]
results = {condition: {"bubble_sort": [], "sorted()": []} for condition in conditions}

for condition in conditions:
    for size in sizes:
        arr = generate_array(size, condition)
        results[condition]["bubble_sort"].append(measure_time(lambda a: bubble_sort(a.copy()), arr))
        results[condition]["sorted()"].append(measure_time(lambda a: sorted(a), arr))

# Pygame visualization
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Sorting Algorithm Execution Time")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
font = pygame.font.Font(None, 24)

def draw_graph():
    screen.fill(WHITE)
    max_time = max(max(results[cond]["bubble_sort"] + results[cond]["sorted()"]) for cond in conditions)
    scale = 500 / max_time  # Scale for graph height
    
    for c_idx, condition in enumerate(conditions):
        for i, size in enumerate(sizes):
            x = 100 + i * 120 + c_idx * 40
            pygame.draw.line(screen, RED, (x, 550), (x, 550 - results[condition]["bubble_sort"][i] * scale), 5)
            pygame.draw.line(screen, BLUE, (x + 10, 550), (x + 10, 550 - results[condition]["sorted()"][i] * scale), 5)
            text = font.render(str(size), True, (0, 0, 0))
            screen.blit(text, (x, 560))
    
    pygame.display.flip()

draw_graph()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(30)

pygame.quit()
