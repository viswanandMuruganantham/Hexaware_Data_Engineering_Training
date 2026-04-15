nums = [34,6,23,8]
min = nums[0]
for i in range(1,len(nums)):
    if nums[i] < min:
        min = nums[i]
print(min)
