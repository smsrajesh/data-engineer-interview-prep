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


# ===================================================
# Approach 2: Hash Map (Frequency Dictionary)
# ===================================================
#
# Idea:
# 1. Count the frequency of every character in s.
# 2. Traverse t and decrement the frequency.
# 3. If a character is missing, return False.
# 4. Remove characters whose count becomes zero.
# 5. If the dictionary becomes empty, return True.
#
# Time Complexity : O(n)
#
# Space Complexity: O(n)
#
# ===================================================

def approach_2(s, t):

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:

        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0


