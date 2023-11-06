def arr_sum(arr, n):
    if n<=0:
        return 0
    
    else:
        return arr[n-1] + arr_sum(arr, n-1)
    
    
arr_str = input('Enter the space separated numbers for the array: ')

arr = [int(x) for x in arr_str.split()]

result = arr_sum(arr, len(arr))
print(f'The sum of the array is: {result}')