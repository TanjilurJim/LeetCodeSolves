# 136. Single Number
# Given a non-empty array of integers nums,
# every element appears twice except for one.
# Find that single one.
#
# You must implement a solution with a linear
# runtime complexity and use only constant extra space.
#Example 1:
# Example 1:
#
# Input: nums = [2,2,1]
# Output: 1
# asdf
#will use X-OR bitwise operation
# 0 x 0 = 0
# 1 x 1 = 0
# 1 x 0 = 1
def singleNumber(nums):
    res = 0
    for n in nums:
        res = n ^ res
    return res


n = [1,2,2]

print(singleNumber(n))



