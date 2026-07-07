# Linear Search
def linear_search_sorted_words(word_list, target_word):
    steps = 0
    
    for i in range(len(word_list)):
        steps += 1
        
        if word_list[i] == target_word:
            return i, steps
        
    return -1, steps
    

# Binary Search
def binary_search_sorted_words(word_list, target_word):
    left_point = 0
    right_point = len(word_list)
    steps = 0
    
    while left_point <= right_point:
        middle_point = (left_point + right_point) // 2
        steps +=1
        
        if word_list[middle_point] < target_word:
            left_point = middle_point + 1
            
        elif word_list[middle_point] > target_word:
            right_point = middle_point - 1
            
        else:
            return middle_point, steps
        
    return -1, steps

# Scenario 2 Test
sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry']
target_2 = 'orange'
result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)
print(f"Scenario 2 (Linear Search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")