"""
Two Number Sum
 Write a function that takes in a non-empty array of distinct integers and an integer
 representing a target sum. If any two numbers in the input array sum up to the target sum,
 the function should return them in an array, in any order. If no two numbers sum up to the
 target sum, the function should return an empty array.
 Note that the target sum has to be obtained by summing two different integers in the array;
 you can't add a single integer to itself in order to obtain the target sum.
 
 You can assume that there will be at most one pair of numbers summing up to the target
 sum
"""
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     result = []
#     for i in range(len(array)):
#         for j in range(len(array)):
#             if array[i] + array[j] == targetSum:
#                 if array[i] != array[j]:
#                     result = [array[i], array[j]]
#                     break
#     return result

"""
Pretty straightforward solution - store all values from array in a set. Then loop through each number in the array, looking for its pair in the set. If it's there we return the two numbers, otherwise loop exits and empty array is returned.
"""
def twoNumberSum(array, targetSum):
    storage = set(num for num in array)
    for num in array:
        target = targetSum - num
        if target in storage and target is not num:
             return [num, target]
    return []

array = [- 3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print(twoNumberSum(array, targetSum))