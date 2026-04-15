nums = [23,56,1,78,3]
max = nums[0]
for i in range(1,len(nums)):
    if nums[i] > max:
        max = nums[i]
print(max)