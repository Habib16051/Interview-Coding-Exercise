def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
        
    return result


nums = [2,2,1,1,5,5,7,7,8]
result = single_number(nums)
print(result)