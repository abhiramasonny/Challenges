"""
Challenge: Longest Increasing Subarray

Given an array of integers, write a Python function to find the length of the longest increasing subarray.

Function Signature: def longest_increasing_subarray(arr: List[int]) -> int:

Input:

arr: A list of integers, where 1 <= len(arr) <= 10^5, and -10^9 <= arr[i] <= 10^9
Output:

An integer, representing the length of the longest increasing subarray.
Example:

Input: arr = [1, 3, 2, 5, 8, 7, 9]
Output: 3
Explanation: The longest increasing subarray is [2, 5, 8] with a length of 3.

Input: arr = [1, 2, 3, 4, 5]
Output: 5
Explanation: The entire array is an increasing subarray with a length of 5.

Input: arr = [5, 4, 3, 2, 1]
Output: 1
Explanation: Each element in the array is an increasing subarray with a length of 1.

Note:

The subarray must be strictly increasing, i.e., the elements must be in strictly ascending order.
Your solution should have a time complexity of O(n), where n is the length of the input array.

"""
from typing import List

def longest_increasing_subarray(arr: List[int]) -> int:
    def test(x, mostc):
        if x == 0:
            return mostc
        elif arr[x] > arr[x-1]:
            return test(x-1, mostc+1)
        else:
            return test(x-1, 1)

    longest_len = 0
    for i in range(len(arr)):
        longest_len = max(longest_len, test(i, 1))
    
    return longest_len

print(longest_increasing_subarray([0,6,2,3,2,4])) # Output: 3
