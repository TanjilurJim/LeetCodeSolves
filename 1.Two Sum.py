class Solution:

    ##TC : O(n)
    ##SC : O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in num_map:
                return [num_map[complement], index]
            num_map[value] = index







