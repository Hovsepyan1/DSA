def merge(arr, left, middle, right):
    l1 = left
    l2 = middle + 1
    r1 = middle
    r2 = right
    tmp = []
    
    while l1 <= r1 and l2 <= r2:
        if arr[l1] <= arr[l2]:
            tmp.append(arr[l1]) 
            l1 += 1
        else:
            tmp.append(arr[l2])
            l2 += 1
            
    while l1 <= r1:
        tmp.append(arr[l1])
        l1 += 1

    while l2 <= r2:
        tmp.append(arr[l2])
        l2 += 1
        
    for i in range(len(tmp)):
        arr[left + i] = tmp[i]
        
        
def merge_sort(arr, left, right):
    if left >= right:
        return 
    
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

    
arr = [i for i in range(1000,0,-1)]
# print(arr)
merge_sort(arr, 0, len(arr) - 1)
print(arr)