# Insertion Sort

nums = [78, 19, 44, 17, 25, 11, 92, 29, 61, 87]
for i in range(len(nums)):
        for j in range(1, len(nums)):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]

print(nums)