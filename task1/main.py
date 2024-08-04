import timeit
import numpy as np


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def tim_sort(arr):
    sorted(arr)


# Функція для вимірювання часу виконання
def measure_time(sort_function, data):
    start_time = timeit.default_timer()
    sort_function(data)
    end_time = timeit.default_timer()
    return end_time - start_time


sizes = [100, 1000, 5000, 10000, 20000]
results = []

for size in sizes:
    data = np.random.randint(0, 10000, size).tolist()

    data_merge = data.copy()
    data_insertion = data.copy()
    data_timsort = data.copy()

    time_merge = measure_time(merge_sort, data_merge)

    time_insertion = measure_time(insertion_sort, data_insertion)

    time_timsort = measure_time(tim_sort, data_timsort)

    results.append(
        [size, f"{time_merge:.6f}", f"{time_insertion:.6f}", f"{time_timsort:.6f}"]
    )

print(f"{'Size':<10} {'Merge Sort (s)':<20} {'Insertion Sort (s)':<20} {'Timsort (s)'}")
print("-" * 60)

for result in results:
    size, merge_time, insertion_time, timsort_time = result
    print(f"{size:<10} {merge_time:<20} {insertion_time:<20} {timsort_time}")
