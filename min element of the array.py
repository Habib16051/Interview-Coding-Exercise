def find_min(arr,n):
    if n == 1:
        return arr[0]
    
    else:
        min_rest = find_min(arr, n-1)
        return min_rest if min_rest < arr[n-1] else arr[n-1]

arr_str = input('Enter the space separated element for the array: ')

arr = [int(x) for x in arr_str.split()]

result = find_min(arr, len(arr))
print('The minimum number of elements of the array is: ', result)