import time
from .bubble_sort import bubble_sort
from .heap_sort import heapsort
from .selection_sort import selection_sort
from .insertion_sort import insertion_sort
from .merge_sort import merge_sort
from .quick_sort import QuickSort
from .radix_sort import countingSort


def sample_main():

    input_string = input("Enter a list element separated by space ")
    list  = input_string.split()
    numbers = [ int(x) for x in list ]

    print("\n\n")

    st = time.time()
    print("Bubble Sort ",bubble_sort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Bubble Sort Execution time:', elapsed_time, 'seconds')

    print("\n")
    print("--------------------------------------")

    st = time.time()
    print("Heap Sort", heapsort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Heap Sort Execution time:', elapsed_time, 'seconds')

    print("\n")
    print("--------------------------------------")

    st = time.time()
    print("Selection Sort", selection_sort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Selection Sort Execution time:', elapsed_time, 'seconds')

    print("\n")
    print("--------------------------------------")

    st = time.time()
    print("Insertion Sort", insertion_sort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Insertion Sort Execution time:', elapsed_time, 'seconds')

    print("\n")
    print("--------------------------------------")

    st = time.time()
    temp = numbers
    merge_sort(temp, 0 , len(temp)-1)
    print("Merge Sort ", temp)
    et = time.time()
    elapsed_time = et - st
    print('Merge Sort Execution time:', elapsed_time, 'seconds')

    print("\n")
    print("--------------------------------------")


    st = time.time()
    print("Quick Sort", QuickSort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Quick Sort Execution time:', elapsed_time, 'seconds')


    print("\n")
    print("--------------------------------------")

    st = time.time()
    print("Radix Sort",countingSort(numbers))
    et = time.time()
    elapsed_time = et - st
    print('Radix Sort Execution time:', elapsed_time, 'seconds')


    print("\n")
    print("--------------------------------------")

