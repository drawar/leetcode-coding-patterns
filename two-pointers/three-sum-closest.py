# https://leetcode.com/problems/3sum-closest/

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if sum < target:
                    lo += 1
                elif sum > target:
                    hi -= 1
                else:
                    return target
                # this allows us to keep track of a minimum value of diff
                # we can also keep track of the value of sum associated with min diff
                if abs(target - sum) < abs(diff):
                    diff = target - sum
        return target - diff

# Time complexity: Time complexity: $O(n^2)$. We have outer and inner loops, each going through $n$ elements.
# Sorting the array doesn't change the overall asymptotic complexity.
# Space complexity: $O(1)$.