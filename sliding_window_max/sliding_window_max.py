# debug = True

'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # if debug: print(f"nums\t{nums}")
    # l = len(nums)
    m = max(nums[:k])
    result = [m]
    # for i in range(1+l-k):
    for i in range(k,len(nums)):
        if nums[i] > m:
            m = nums[i]
            # if debug: print(f"segment\t{m}")
        # else:
            # segment = nums[i:i+k]
            # segment = nums[i-k+1:i+1]
            # if debug: print(f"segment\t{segment}")
            # m = max(segment)
        elif m == nums[i-k]:
            m = max(nums[i-k+1:i+1])
        # if debug: print(f"max\t{m}")
        result.append(m)
    
    # if debug: print(f"result\t{result}")
    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
