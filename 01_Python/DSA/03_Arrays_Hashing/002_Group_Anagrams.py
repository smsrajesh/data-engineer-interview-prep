# ===================================================
# Problem: Group Anagrams
# Category: Arrays & Hashing
# Difficulty: Medium
# ===================================================

# Problem Statement:
#
# Given an array of strings, group the anagrams together.
# You can return the answer in any order.
#

# Example:
#
# Input :
# strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]
#
# Explanation:
# Strings having the same characters with the same
# frequency belong to the same group.
#

# ===================================================
# Approach 1: Sorting
# ===================================================
#
# Idea:
# 1. Traverse each word in the list.
# 2. Sort the characters of the word.
# 3. Use the sorted string as the dictionary key.
# 4. Append the original word to the corresponding list.
# 5. Return all grouped values.
#
# Time Complexity : O(n × k log k)
#
# Space Complexity: O(n × k)
#
# ===================================================

def approach_1(strs):

    groups = {}

    for word in strs:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# ===================================================
# Approach 2: Frequency Count
# ===================================================
#
# Idea:
# 1. Traverse each word.
# 2. Create a frequency array of size 26.
# 3. Count the occurrences of every character.
# 4. Convert the frequency array into a tuple.
# 5. Use the tuple as the dictionary key.
#
# Time Complexity : O(n × k)
#
# Space Complexity: O(n × k)
#
# Note:
# Works only for lowercase English letters.
#
# ===================================================

def approach_2(strs):

    groups = {}

    for word in strs:

        count = [0] * 26

        for ch in word:
            index = ord(ch) - ord('a')
            count[index] += 1

        key = tuple(count)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# ===================================================
# Test Cases
# ===================================================

# Test Case 1

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(approach_1(strs))
print(approach_2(strs))


# Test Case 2

strs = [""]

print(approach_1(strs))
print(approach_2(strs))


# Test Case 3

strs = ["a"]

print(approach_1(strs))
print(approach_2(strs))


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Two strings are anagrams if they contain the same
#   characters with the same frequency.
#
# ✔ Sorting creates a canonical representation of every
#   anagram group.
#
# ✔ Frequency count avoids sorting and gives O(n × k)
#   time complexity.
#
# ✔ Lists are mutable and not hashable, so convert the
#   frequency array to a tuple before using it as a
#   dictionary key.
#
# ✔ Sorting works for any character set (Unicode,
#   uppercase, digits, special characters), whereas the
#   frequency-array approach is limited to lowercase
#   English letters.
#
# ===================================================
# Approach Comparison
# ===================================================
#
# Approach             Time            Space
# ------------------------------------------------
# Sorting              O(n × klogk)   O(n × k)
# Frequency Count      O(n × k)       O(n × k)
#
# Best Choice
#
# ✔ Lowercase English letters
#     → Frequency Count
#
# ✔ Any character set
#     → Sorting
#