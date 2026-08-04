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

# ===================================================
# Approach 3: Frequency Array
# ===================================================
#
# Idea:
# 1. If lengths are different, return False.
# 2. Create a frequency array of size 26.
# 3. Increment counts using characters from s.
# 4. Decrement counts using characters from t.
# 5. If all counts are zero, the strings are anagrams.
#
# Time Complexity : O(n)
#
# Space Complexity: O(1)
#
# Note:
# Works only for lowercase English letters.
#
# ===================================================

def approach_3(s, t):

    if len(s) != len(t):
        return False

    count = [0] * 26

    for ch in s:
        index = ord(ch) - ord('a')
        count[index] += 1

    for ch in t:
        index = ord(ch) - ord('a')
        count[index] -= 1

    return all(value == 0 for value in count)


# ===================================================
# Test Cases
# ===================================================

# Test Case 1
s = "eat"
t = "tea"

print(approach_1(s, t))
print(approach_2(s, t))
print(approach_3(s, t))


# Test Case 2
s = "rat"
t = "car"

print(approach_1(s, t))
print(approach_2(s, t))
print(approach_3(s, t))


# Test Case 3
s = "anagram"
t = "nagaram"

print(approach_1(s, t))
print(approach_2(s, t))
print(approach_3(s, t))


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Brute Force: Sort both strings and compare.
#
# ✔ Hash Map: Count character frequencies and compare.
#
# ✔ Frequency Array: Best for lowercase English letters.
#
# ✔ Tuple is hashable; list is not hashable.
#
# ✔ Sorting works for any character set, while the
#   frequency array is limited to lowercase English letters.
#
# ✔ Follow-up:
#   - Unicode characters → Use sorting or HashMap.
#   - Lowercase English letters only → Frequency array.


# ===================================================
# Approach Comparison
# ===================================================
#
# Approach         Time        Space      Best Use Case
# ----------------------------------------------------
# Sorting          O(nlogn)    O(n)       Any characters
# HashMap          O(n)        O(n)       General purpose
# Frequency Array  O(n)        O(1)       Lowercase letters only
#

