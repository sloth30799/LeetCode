# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

nums = [1,2,3,4,5,6,7]
k = 3


def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0:
        return

    for i in range(k):
        num = nums[len(nums) - 1]

        nums.pop()
        nums.insert(0, num)

        print(nums)


# optimized version
def rotateV2(nums: list[int], k: int) -> None:
    if k == 0:
        return

    size = len(nums)
    k = k if k <= size else k % size

    print(nums[k:])
    print(nums[:size - k])
    nums[k:], nums[:k] = nums[:size - k], nums[size - k:]


# rotate(nums, k)
rotateV2(nums, k)
