**SELECTION SORT CORRECTNESS**

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:  
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

loop invariant: At the start of each iteration of the first loop for each i the sub array goes from 0 to i-1 , which is already sorted. The smallest element from the array which is 
