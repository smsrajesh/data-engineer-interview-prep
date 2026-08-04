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
