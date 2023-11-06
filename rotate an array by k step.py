def rotate_array(nums, k):
    n = len(nums)
    k = k % n  # Handle cases where k is larger than the length of the array
    if n <= 1 or k == 0:
        return nums  # No rotation needed

    # Split the array into two parts and reverse them
    nums[:n - k], nums[n - k:] = nums[:n - k][::-1], nums[n - k:][::-1]
    # Reverse the entire array
    nums[:] = nums[::-1]
    return nums


# Example usage:
original_array = [1, 2, 3, 4, 5]
k = 3
rotated_array = rotate_array(original_array, k)
print(rotated_array)
