# Linear Search
def linear_search_unsorted(arr, target):
    steps = 0
    
    for i in range(len(arr)):
        steps += 1
        
        if arr[i] == target:
            return i, steps
        
    return -1, steps

# Binary Search
def binary_search_unsorted(arr, target):
    left_point = 0
    right_point = len(arr) - 1
    steps = 0
    
    while left_point <= right_point:
        middle_point = (left_point + right_point) // 2
        steps += 1
        
        
        if arr[middle_point] < target:
            left_point = middle_point + 1
            
        elif arr[middle_point] > target:
            right_point = middle_point - 1
            
        else:
            return middle_point, steps
        
    return -1, steps
    pass

# Scenario 1 Test
unsorted_list = [42, 15, 7, 30, 22, 10, 18]
target_1 = 30
result_linear_search_1 = linear_search_unsorted(unsorted_list, target_1)
result_binary_search_1 = binary_search_unsorted(sorted(unsorted_list), target_1)
print(result_linear_search_1)
print(result_binary_search_1)
print(f"Scenario 1 (Linear Search): Target {target_1} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 1 (Binary Search): Target {target_1} found at index {result_binary_search_1[0]} in {result_binary_search_1[1]} steps.")