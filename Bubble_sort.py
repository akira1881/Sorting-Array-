# Bubble Sort

def sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range (i):
            if nums[j]> nums [j+1]:
                temp = nums[j]
                temp = nums[j]
                nums[j+1] = temp


nums = [78, 19, 44, 17, 25, 11, 92, 29, 61, 87]
sort(nums)

print(nums)