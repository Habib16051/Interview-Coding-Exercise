def remove_duplicate(arr):
    unique_arr = []
    
    for item in arr:
        if item not in unique_arr:
            unique_arr.append(item)
            
    return unique_arr


input_str = input('Enter the elements of the array:  ')

input_arr = [int(x) for x in input_str.split()]

result = remove_duplicate(input_arr)


print(f'Your unique array after removing the duplicates: {result}')