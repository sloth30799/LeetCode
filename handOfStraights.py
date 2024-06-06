# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.


def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    arr_count = int(len(hand) / groupSize)
    res = [[]] * arr_count

    for i in range(arr_count):
        for j in range(groupSize):
            if len(res[i]) == 0:
                res[i] = []
                res[i].append(min(hand))
                hand.remove(min(hand))
            else:
                num = max(res[i]) + 1

                if num in hand:
                    res[i].append(num)
                    hand.remove(num)
                else:
                    return False

    return True


hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
print(isNStraightHand(hand, 3))
