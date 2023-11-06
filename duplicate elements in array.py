def find_duplicate(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)  # If no duplicates are found

# Get user input for the array
arr_str = input("Enter space-separated numbers for the array: ")
numbers = [int(x) for x in arr_str.split()]

duplicate_numbers = find_duplicate(numbers)
if duplicate_numbers:
    print("Duplicate number:", duplicate_numbers)
else:
    print("No duplicates found")
