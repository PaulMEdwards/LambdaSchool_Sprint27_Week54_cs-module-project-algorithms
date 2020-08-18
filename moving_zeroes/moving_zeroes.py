'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr = []):
    i = 0
    for v in arr:
        if v != 0:
            n = arr.pop(i)
            arr.insert(0, n)
        i += 1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")