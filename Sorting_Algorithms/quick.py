from random import randint

def partition_first(arr, low, high):
    i = low + 1
    j = high
    while i <= j:
        if arr[i] <= arr[low]:
            i += 1
        elif arr[j] > arr[low]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[low], arr[j] = arr[j], arr[low]
    return j

def partition_last(arr, low, high):
    i = low
    j = high - 1
    
    while i <= j:
        if arr[i] <= arr[high]:
            i += 1
        elif arr[j] > arr[high]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[high], arr[i] = arr[i], arr[high]
    return i 

def partition_last_two(arr, low, high):
    i = low 
    pi = arr[high]
    for j in range(low, high):
        if arr[j] <= pi:
            arr[i] , arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i 

def find_pivot(arr, low, high):
    mid = low + (high - low) // 2
    if (arr[low] > arr[mid] and arr[high] < arr[mid]) or (arr[low] < arr[mid] and arr[high] > arr[mid]):
        return mid
    elif (arr[mid] > arr[low] and arr[low] < arr[high]) or (arr[mid] < arr[low] and arr[low] > arr[high]):
        return low
    else: 
        return high
    
    
def partition_median(arr, low, high):
    pi = find_pivot(arr, low, high)
    arr[pi], arr[high] = arr[high], arr[pi]
    i = low
    j = high - 1
    
    while i <= j:
        if arr[i] <= arr[high]:
            i += 1
        elif arr[j] > arr[high]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[high], arr[i] = arr[i], arr[high]
    return i 

def partition_random(arr, low, high):
    pi = randint(low, high)
    arr[pi], arr[high] = arr[high], arr[pi]
    i = low
    j = high - 1
    
    while i <= j:
        if arr[i] <= arr[high]:
            i += 1
        elif arr[j] > arr[high]:
            j -= 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
            
    arr[high], arr[i] = arr[i], arr[high]
    return i 

def quick_sort(arr, low, high):
    if low < high:
        pi = partition_random(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
        
        
arr = [10,7,8,9,1,5]
quick_sort(arr, 0, len(arr) - 1)
print(arr)