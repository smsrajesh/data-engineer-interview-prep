# ===================================================
# Problem: Valid Anagram
# Category: Arrays & Hashing
# Difficulty: Easy
# ===================================================

# Problem Statement:
#
# Given two strings s and t, return True if t is an
# anagram of s, otherwise return False.
#

# Example:
#
# Input :
# s = "eat"
# t = "tea"
#
# Output:
# True
#
# Explanation:
# Both strings contain the same characters with the same frequency.
#

# ===================================================
# Approach 1: Sorting
# ===================================================
#
# Idea:
# 1. Sort both strings.
# 2. Compare the sorted strings.
# 3. If they are equal, the strings are anagrams.
# 4. Otherwise, they are not.
#
# Time Complexity : O(n log n)
#
# Space Complexity: O(n)
#
# ===================================================


def approach_1(s, t):
    if len(s)!=len(t):
        return False
    return sorted(s) == sorted(t)
