def print_subarrays(arr):
    n = len(arr)
    
    for i in range(n):          # starting index
        for j in range(i, n):   # ending index
            for k in range(i, j + 1):  # print elements
                print(arr[k], end=" ")
            print()  # new line for next subarray

# Example
arr = [1, 2, 3]
print_subarrays(arr)
