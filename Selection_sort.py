# Selection Sort

def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i, 10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp
        print(nums)

nums = [78, 19, 44, 17, 25, 11, 92, 29, 61, 87]
sort(nums)

print(nums)

