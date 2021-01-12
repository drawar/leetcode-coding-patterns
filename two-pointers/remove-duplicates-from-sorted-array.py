# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 1
        while i < j and j < len(nums):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i + 1
