# ===================================================
# Problem: Two Sum
# Category: Arrays & Hashing
# Difficulty: Easy
# ===================================================

# Problem Statement:
#
# Given an array of integers nums and an integer target,
# return the indices of the two numbers such that they
# add up to the target.
#
# You may assume that each input has exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.
#

# Example:
#
# Input :
# nums = [2,7,11,15]
# target = 9
#
# Output:
# [0,1]
#
# Explanation:
# nums[0] + nums[1] = 2 + 7 = 9
#

# ===================================================
# Approach 1: Brute Force
# ===================================================
#
# Idea:
# 1. Traverse every element in the array.
# 2. Compare it with every remaining element.
# 3. If their sum equals the target,
#    return their indices.
#
# Time Complexity : O(n²)
#
# Space Complexity: O(1)
#
# ===================================================

def approach_1(nums, target):

    n = len(nums)

    for i in range(n):

        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# ===================================================
# Approach 2: Hash Map (Optimal)
# ===================================================
#
# Idea:
# 1. Create an empty HashMap.
# 2. Traverse the array once.
# 3. Calculate the complement:
#
#       complement = target - current number
#
# 4. If the complement already exists,
#    return the stored index and current index.
# 5. Otherwise, store the current number
#    and its index in the HashMap.
#
# Time Complexity : O(n)
#
# Space Complexity: O(n)
#
# ===================================================

def approach_2(nums, target):

    hashmap = {}

    for index, num in enumerate(nums):

        complement = target - num

        if complement in hashmap:
            return [hashmap[complement], index]

        hashmap[num] = index

    return []


# ===================================================
# Approach 3: Brute Force (All Possible Index Pairs)
# ===================================================
#
# Idea:
# 1. Traverse every element in the array.
# 2. Compare it with every remaining element.
# 3. If their sum equals the target,
#    store the pair of indices.
# 4. Continue until every possible pair
#    has been checked.
#
# Time Complexity : O(n²)
#
# Space Complexity: O(k)
#
# where k = number of valid pairs.
#
# ===================================================

def approach_3(nums, target):

    result = []

    n = len(nums)

    for i in range(n):

        for j in range(i + 1, n):

            if nums[i] + nums[j] == target:

                result.append([i, j])

    return result


# ===================================================
# Test Cases
# ===================================================

# Test Case 1
#
# Input:
# nums = [2,7,11,15]
# target = 9
#
# Output:
# Approach 1 -> [0,1]
# Approach 2 -> [0,1]
# Approach 3 -> [[0,1]]

nums = [2,7,11,15]
target = 9

print(approach_1(nums, target))
print(approach_2(nums, target))
print(approach_3(nums, target))


# Test Case 2
#
# Input:
# nums = [3,2,4]
# target = 6
#
# Output:
# Approach 1 -> [1,2]
# Approach 2 -> [1,2]
# Approach 3 -> [[1,2]]

nums = [3,2,4]
target = 6

print(approach_1(nums, target))
print(approach_2(nums, target))
print(approach_3(nums, target))


# Test Case 3
#
# Input:
# nums = [3,3]
# target = 6
#
# Output:
# Approach 1 -> [0,1]
# Approach 2 -> [0,1]
# Approach 3 -> [[0,1]]

nums = [3,3]
target = 6

print(approach_1(nums, target))
print(approach_2(nums, target))
print(approach_3(nums, target))


# Test Case 4
#
# Input:
# nums = [-3,4,3,90]
# target = 0
#
# Output:
# Approach 1 -> [0,2]
# Approach 2 -> [0,2]
# Approach 3 -> [[0,2]]

nums = [-3,4,3,90]
target = 0

print(approach_1(nums, target))
print(approach_2(nums, target))
print(approach_3(nums, target))


# Test Case 5
#
# Input:
# nums = [1,2,3,4,5]
# target = 6
#
# Output:
# Approach 3 -> [[0,4],[1,3]]

nums = [1,2,3,4,5]
target = 6

print(approach_3(nums, target))


# Test Case 6
#
# Input:
# nums = [3,3,3]
# target = 6
#
# Output:
# Approach 3 -> [[0,1],[0,2],[1,2]]

nums = [3,3,3]
target = 6

print(approach_3(nums, target))


# ===================================================
# Interview Notes
# ===================================================
#
# ✔ Brute Force:
#   Compare every possible pair until the target
#   is found.
#
# ✔ Hash Map:
#   Store each number along with its index.
#
# ✔ Instead of searching through the array,
#   calculate the complement:
#
#       complement = target - current_number
#
# ✔ HashMap lookup is O(1), reducing the overall
#   time complexity to O(n).
#
# ✔ The original LeetCode problem guarantees
#   exactly one valid pair.
#
# ✔ If the interviewer asks to return all
#   possible index pairs, continue searching
#   instead of returning immediately.
#
# ✔ Returning all pairs has a worst-case
#   time complexity of O(n²), since the output
#   itself can contain O(n²) pairs.
#
# ✔ Follow-up:
#   - Return all possible index pairs.
#   - Return all unique value pairs.
#   - Solve for a sorted array (Two Sum II).
#   - Solve without extra space.
#

# ===================================================
# Approach Comparison
# ===================================================
#
# Approach                    Time      Space      Best Use Case
# ----------------------------------------------------------------
# Brute Force                 O(n²)     O(1)       Simple solution
# HashMap                     O(n)      O(n)       Interview Optimal
# All Possible Index Pairs    O(n²)     O(k)       Interview Follow-up
#