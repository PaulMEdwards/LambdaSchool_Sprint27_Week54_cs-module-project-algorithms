'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import sys

def max_in_list(nums):
    max = -sys.maxsize - 1
    for n in nums:
        if n > max: max = n
    return max

def sliding_window_max(nums, k):
    # Your code here
    l = len(nums)
    result = []
    for i in range(l+1-k):
        segment = nums[i:i+k]
        result.append(max_in_list(segment))
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
