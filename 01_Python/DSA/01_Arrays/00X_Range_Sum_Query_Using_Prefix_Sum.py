# ============================================================
# Problem: Range Sum Query
# Category: Arrays
# Technique: Prefix Sum
#
# Given an array and multiple ranges [i, j],
# calculate the sum of elements from index i to j (inclusive).
#
# Example:
# a = [2, 3, 1, 5, 4, -3, -5, -7, 8, 9, 6]
# b = [[1, 8], [4, 10], [6, 7]]
#
# Output:
# [6, 12, -12]
#
# ============================================================


# ============================================================
# Approach 1: Brute Force
# ============================================================
#
# For every range:
#   1. Start from index i
#   2. Go until index j
#   3. Add every element
#
# Time Complexity:
#   O(N * Q)
#
# Space Complexity:
#   O(Q)
#
# Where:
#   N = length of array
#   Q = number of queries
# ============================================================

a = [2, 3, 1, 5, 4, -3, -5, -7, 8, 9, 6]
b = [[1, 8], [4, 10], [6, 7]]

result = []

for i, j in b:
    range_sum = 0

    for k in range(i, j + 1):
        range_sum += a[k]

    result.append(range_sum)

print("Brute Force:", result)


# ============================================================
# Approach 2: Prefix Sum
# ============================================================
#
# Build a prefix sum array once.
#
# Prefix Sum:
#   p_sum[i] = sum of elements before index i
#
# Then:
#
#   Sum(i, j) = p_sum[j + 1] - p_sum[i]
#
# The extra 0 at the beginning makes the formula
# work even when i = 0.
#
# Time Complexity:
#   O(N + Q)
#
# Space Complexity:
#   O(N + Q)
# ============================================================

a = [2, 3, 1, 5, 4, -3, -5, -7, 8, 9, 6]
b = [[1, 8], [4, 10], [6, 7]]

# Build prefix sum
p_sum = [0]

for value in a:
    p_sum.append(p_sum[-1] + value)

print("Prefix Sum Array:", p_sum)

# Answer range queries
result = []

for i, j in b:
    result.append(p_sum[j + 1] - p_sum[i])

print("Prefix Sum:", result)



# ============================================================
# Comparison
# ============================================================
#
# Brute Force:
#   Time  : O(N * Q)
#   Space : O(Q)
#
# Prefix Sum:
#   Time  : O(N + Q)
#   Space : O(N + Q)
#
# Preferred Approach:
#   Prefix Sum
#
# Reason:
#   Prefix sum requires O(N) preprocessing, but each
#   range-sum query can then be answered in O(1).
# ============================================================