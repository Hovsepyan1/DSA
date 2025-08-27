def counting_sort(arr):
    print(arr)
    max_element = max(arr)
    
    counting_array = [0] * (max_element + 1)
    for item in arr:
        counting_array[item] += 1
        
    print(counting_array)
    for i in range(1, len(counting_array)):
        counting_array[i] = counting_array[i] + counting_array[i - 1]
    print(counting_array)
    
    output_array = [0] * len(arr)
    i = len(arr) - 1
    while i >= 0:
        output_array[counting_array[arr[i]] - 1] = arr[i]
        counting_array[arr[i]] -= 1
        i -= 1
        
    print(output_array)
    
    #------------------Non-stable------------------
    # index = 0
    # for i in range(len(counting_array)):
    #     while counting_array[i] > 0:
    #         arr[index] = i
    #         index += 1
    #         counting_array[i] -= 1
            
    print(arr)
    
    
arr = [4, 3, 12, 1, 5, 5, 3, 9]
counting_sort(arr)