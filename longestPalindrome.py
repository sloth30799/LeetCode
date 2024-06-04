# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

 

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.

def longest_palindrome(s: str):
    all_count = 0
    flag = False
    chars = set()

    for l in s:
        if l in chars:
            continue

        if s.count(l) % 2 == 0:
            chars.add(l)
            all_count += s.count(l)

        elif flag != True and s.count(l) % 2 != 0:
            chars.add(l)
            all_count += s.count(l)
            flag = True

        elif s.count(l) % 2 != 0:
            chars.add(l)
            all_count += s.count(l) - 1

    return all_count

# better solution
def longestPalindrome(self, s: str) -> int:

    pair_counter = 0
    chars = set()

    for ch in s:
        if ch in chars:
            chars.remove(ch)
            pair_counter += 1

        else:
            chars.add(ch)

    return pair_counter * 2 + (1 if len(chars) > 0 else 0)


print(longest_palindrome('abccccdd'))
