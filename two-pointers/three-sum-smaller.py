# https://leetcode.com/problems/3sum-smaller/

from typing import List
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            count += self.twoSumSmaller(nums, i + 1, target - nums[i])
        return count

    def twoSumSmaller(self, nums: List[int], start: int, target: int) -> int:
        count = 0
        left, right = start, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count

# Time complexity: $O(n^2)$ since threeSumSmaller calls twoSumSmaller `n` times, and twoSumSmaller is
# $O(n)$ since both left and right traverse at most `n` steps.
# Space complexity: $O(1)$.
