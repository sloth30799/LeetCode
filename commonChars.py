# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]


def commonChars(words: list[str]) -> list[str]:
    result = []
    chars = set()

    for ch in words[0]:
        if ch not in chars:
            count = min(map(lambda x: x.count(ch), words))
            chars.add(ch)
            result += [ch] * count

    return result


words1 = ["bella", "label", "roller"]
words2 = ["cool", "lock", "cook"]

commonChars(words2)
