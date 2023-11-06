arr_str = input('Enter the space separated element of the array: ')
arr = [int(x) for x in arr_str.split()]
result = sorted(arr)

print('The sorted array is: ', result)