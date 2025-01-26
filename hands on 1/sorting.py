import time
import random
import matplotlib.pyplot as plt
import psutil
from GPUtil import getGPUs


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:  
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Bubble Sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
# Laptop Benchmarks
def laptop_benchmarks():
    print("\n=== Laptop Benchmarks ===")
    # CPU Usage
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")

    # Memory Usage
    memory = psutil.virtual_memory()
    print(f"Memory Usage: {memory.used / (1024 ** 3):.2f} GB / {memory.total / (1024 ** 3):.2f} GB")

    # Clock Speed
    cpu_freq = psutil.cpu_freq()
    if cpu_freq:
        print(f"Current Clock Speed: {cpu_freq.current:.2f} MHz")

    # Disk Usage
    disk = psutil.disk_usage('/')
    print(f"Storage Usage: {disk.used / (1024 ** 3):.2f} GB / {disk.total / (1024 ** 3):.2f} GB")

    # GPU Usage
    gpus = getGPUs()
    if gpus:
        for gpu in gpus:
            print(f"GPU: {gpu.name}")
            print(f"GPU Usage: {gpu.load * 100:.2f}%")
            print(f"GPU Memory Usage: {gpu.memoryUsed / 1024:.2f} GB / {gpu.memoryTotal / 1024:.2f} GB")
    else:
        print("No GPU")


# Benchmarking Function
def benchmark_sorting_algorithm(algorithm, sizes):
    times = []
    for size in sizes:
        start = time.time()
        algorithm(random.sample(range(1, size * 10), size))
        end = time.time()
        times.append(end - start)
    return times

# Input Sizes
sizes = [random.randint(5, 10000) for _ in range(5)] 

# Run Benchmarks
insertion_times = benchmark_sorting_algorithm(insertion_sort, sizes)
selection_times = benchmark_sorting_algorithm(selection_sort, sizes)
bubble_times = benchmark_sorting_algorithm(bubble_sort, sizes)

# Plotting the Results
plt.plot(sizes, insertion_times, label="Insertion Sort", marker='o')
plt.plot(sizes, selection_times, label="Selection Sort", marker='o')
plt.plot(sizes, bubble_times, label="Bubble Sort", marker='o')
plt.xlabel('Input Size n')
plt.ylabel('Time t')
plt.title('Sorting Algorithm time vs input size graph')
plt.legend()
plt.grid(True)
plt.show()
plt.close()

laptop_benchmarks()




