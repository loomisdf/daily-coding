# This problem was asked by Stripe.
#
# Given an array of integers, find the first missing positive integer in linear time and 
# constant space. In other words, find the lowest positive integer that does not exist in the 
# array. The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.
array1 = [3, 4, -1, 0, 2]
array2 = [1, 2, 0]
array3 = [1, 1, 5, 6, 8, 7, 3, 2, 2, 0, -1]

def firstMissingPositive(array):
    list.sort(array)
    i = 1
    while i < len(array):
        if array[i] > 1:
            if array[i] - array[i-1] > 1:
                return array[i] - 1
        i += 1
    return array[len(array) - 1] + 1

def firstMissingHashTable(list):
    hashTable = {}
    for num in list:
        if num >= 1:
            hashTable[num] = num

    i = 1
    while True:
        if i not in hashTable:
            return i
        i += 1


# print(firstMissingPositive(array1))
# print(firstMissingPositive(array2))
# print(firstMissingPositive(array3))
# print(firstMissingHashTable([0, 1, 3, 7, 6, 8, -1, -10, 15]))
print(firstMissingHashTable([0, 1, 2, 3, 4, 6]))