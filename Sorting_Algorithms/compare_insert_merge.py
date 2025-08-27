import time

def time_it(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = fn(*args, **kwargs)
        end = time.time()
        elipsis = end - start
        print(f"The {fn.__name__} takes {elipsis:.6f} minute")
        return res
    return wrapper

@time_it
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr
        
        
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[left + i]
    for j in range(n2):
        R[j] = arr[mid + 1 + j]

    i = 0  
    j = 0  
    k = left  
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    
@time_it
def merge_helper(arr, left, right):
    return mergeSort(arr, left, right)

arr = [i for i in range(60,0,-1)]
arr1 = [i for i in range(60,0,-1)]
# print(arr1)

# print(arr)
insertion_sort(arr)
merge_helper(arr1, 0, len(arr1) - 1)
# print(arr1)
