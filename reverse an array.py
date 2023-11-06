def reverse_arr(arr):
    # Using slice to reverse the array
    return arr[::-1]


arr_str = input('Enter space separated element for the array: ')

arr = [int(x) for x in arr_str.split()]

result = reverse_arr(arr)

print('The reverse array is: ', result)