#-*- coding: utf-8 -*-

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        
        else:
            low = mid + 1
    return None

def normal_search(list, item):
    # for i in range(len(list)):
    #     if list[i] == item:
    #         return i

    for i, value in enumerate(list):
        if value == item:
            return i

    return None

my_list = [1, 3, 5, 7, 9]

print(normal_search(my_list, 3))
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
