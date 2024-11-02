# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

def canJump(nums: list[int]) -> bool:
    destination = len(nums) - 1
    farthest = 0

    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
        if farthest >= destination:
            return True

    return False
