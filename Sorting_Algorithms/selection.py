def min_element(arr):
    min = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i
            
    return index

def selection_sort(arr):
    sorted = []
    while arr != []:
        key = min_element(arr)
        sorted.append(arr[key])
        arr.pop(key)
        
    return sorted

arr = [i for i in range(10,0,-1)]
print(selection_sort(arr))