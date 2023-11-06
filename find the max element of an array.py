def find_max(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_rest = find_max(arr, n - 1)
        return max_rest if max_rest > arr[n - 1] else arr[n - 1]

# Get user input for the array
arr_str = input("Enter space-separated numbers for the array: ")
arr = [int(x) for x in arr_str.split()]

result = find_max(arr, len(arr))
print("The maximum element in the array is:", result)
