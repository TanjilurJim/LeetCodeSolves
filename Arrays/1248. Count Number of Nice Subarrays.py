# Given an array of integers nums and an integer k.
# A continuous subarray is called nice if there are k odd numbers
# on it.
#
# Return the number of nice sub-arrays.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are
# [1,1,2,1] and [1,2,1,1].
# Example 2:
#
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

#Topics: Array,Hash Table,Math,Sliding Window

def numberOfSubarrays(nums,k):
    Current_odd_count = 0
    subarrays = 0
    for i in range(len(nums)):
        count = 0
        if nums[i]%2 != 0:
            count+=1
            if count == k :
                subarrays +=1
        l+=1





    return subarrays


