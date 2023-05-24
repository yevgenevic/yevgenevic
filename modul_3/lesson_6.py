# s = 'hello world'
# most_common = max(set(s),key=s.count)
# print(most_common)

# from itertools import groupby
# s = 'hello ttttttttttttttttttworld'
# q = groupby(sorted(s))
# mst = max(q,key=lambda i: len(list(i[1])))
# m = mst[0]
# result.append(str(nums[start]))
# else:
# result.append(str(nums[start]) + "->" + str(nums[i]))
# print(len(mst))
# if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
#     continue


nums = [0, 1, 2, 4, 5, 7]
start_index = 0
result = []
for i in range(len(nums)):
    if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
        continue
    if start_index == i:
        result.append(str(nums[start_index]))
    else:
        result.append(str(nums[start_index]) + "->" + str(nums[i]))
    start_index = i + 1
print(result)
# s = "ab"
# goal = "ba"
# if s[0]==goal[1] and s[1]==goal[0]:
#     print(True)
# else:
#     print(False)
#



