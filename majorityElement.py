# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

def majorityElement(nums: list[int]) -> int:
    halfLenOfList = len(nums) / 2
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

        if counts[num] > halfLenOfList:
            return num


nums = [3, 2, 3]

print(majorityElement(nums))
