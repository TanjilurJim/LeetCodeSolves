from typing import List
class Solution:


    ##TC : O(n)
    ##SC : O(n)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  #val:index

        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return










if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()  # create an instance
    print(s.twoSum(nums, target))