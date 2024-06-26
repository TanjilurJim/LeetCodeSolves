#Given an integer array nums sorted in non-decreasing order
# , return an array of the squares of each number sorted in
# non-decreasing order.


#
# Example 1:
#
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:
#
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

class Solution:
    #t.c = O(nlogn)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqrd = [x ** 2 for x in nums]
        sqrd.sort()
        return sqrd


#Two Pointer Approach: T.C = O(n), S.C = O(n)

    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []

        l, r = 0, len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.append((abs(nums[l] * nums[l])))
                l += 1
            else:
                result.append((abs(nums[r] * nums[r])))
                r -= 1

        return result[::-1]


