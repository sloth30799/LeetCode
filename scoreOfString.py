# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
# Return the score of s.


# Example 1:
# Input: s = "hello"
# Output: 13
# Explanation:
# The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

# Example 2:
# Input: s = "zaz"
# Output: 50
# Explanation:
# The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.

def scoreOfString(s: str) -> int:
    prev = ord(s[0])
    result = 0

    for count, ele in enumerate(s):
        if (count > 0):
            result += abs(prev - ord(ele))

            prev = ord(ele)

    return result

# better
def scoreOfStringv2(s: str) -> int:
    result = 0

    for i in range(1,len(s)):
        result += abs(ord(s[i-1]) - ord(s[i]))

    return result


text = "zaz"
scoreOfString(text)
print(scoreOfStringv2(text))
