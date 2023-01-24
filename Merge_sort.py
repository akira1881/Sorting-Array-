# Merge Sort

def sort(nums):
    if len(nums) <= 1:
        return

    mid = len(nums)//2

    left = nums[:mid]
    right = nums[mid:]

    sort(left)
    sort(right)

    sorted_lists(left, right, nums)


def sorted_lists(a, b, nums):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            nums[k] = a[i]
            i += 1

        else:
            nums[k] = b[j]
            j += 1
        k += 1
    
    while i < len_a:
        nums[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        nums[k] = b[j]
        j += 1
        k += 1


if __name__ == '__main__':
    num_list = [
        [78, 19, 44, 17, 25, 11, 92, 29, 61, 87]
    ]

    for nums in num_list:
        sort(nums)
        print(nums)
