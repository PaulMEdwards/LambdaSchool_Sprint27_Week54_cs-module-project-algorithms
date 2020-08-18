debug = False

'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    result = []
    for n in arr:
        if debug: print(f"n: {n}")
        r = -1
        try:
            r = result.index(n)
        except ValueError:
            pass
        finally:
            if debug: print(f"r: {r}")
            if r >= 0:
                result.remove(n)
            else:
                result.append(n)
        if debug: print(result)

    return result[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")