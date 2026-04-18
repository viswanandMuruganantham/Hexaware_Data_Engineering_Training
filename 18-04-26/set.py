nums = {1,2,3,4,5,6,7,8,9}
print(nums)

nums = [2,2,33,33,55,55]

u_nums = set(nums)
print(u_nums)

u_nums.add(5)
print(u_nums)
u_nums.update([30,40,50])
print(u_nums)

set1 = {20,30,40,50}
set2 = {30,50,60,70}
res = set1.union(set2)
print(res)
res = set1.difference(set2)
print(res)
res = set1.intersection(set2)
print(res)
