# Given an integer array nums, return true
# if any value appears at least twice in the array, and
# return false if every element is distinct.

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False


# l = [1,1,1,3,3,4,3,2,4,2]
l = [1,2,3,4]
print(containsDuplicate(l))



