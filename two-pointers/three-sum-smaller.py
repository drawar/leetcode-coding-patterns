# https://leetcode.com/problems/3sum-smaller/

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
