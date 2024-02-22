def add(*nums):
    total=0
    for i in range(len(nums)):
        for num in nums[i]:
            total+=num

    return total
print(add([4,3,2],[9,8,7]))