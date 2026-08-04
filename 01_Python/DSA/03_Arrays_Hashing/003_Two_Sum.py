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