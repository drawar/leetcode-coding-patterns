# https://leetcode.com/problems/subarray-product-less-than-k/

# Note that the two pointer solution only works because all elements in the array are strictly positive.
# We also assume that the product of all array elements fits in 64 bit integer type, so there are no divisions
# by zero, no overflows.

# Between pointers `left` and `right` we have a window, and the product of all elements inside this window is
# `prod < k`. When we try to add a new element `x` by incrementing the `right` pointer (`right` pointer is now
# at `x`), two cases can happen:

# - **Case 1**: `prod * x < k`: we just need to count the number of *incremental* continuous subarrays this step
# produces, which is exactly the length of the window, i.e. `right - left + 1`. After that, we increment `right`.
# - **Case 2**: `prod * x ≥ k`: this means we must first adjust the window's left border so that the product is
# again less than `k`. We do this by discarding the leftmost item one at a time, shrinking the window by 1 at
# each step, until the product of all elements inside the window is less than k. After that, we can apply the
# formula from **Case 1**.

from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        prod = 1
        count = 0
        left = right = 0
        while right < len(nums):
            prod *= nums[right]
            while prod >= k:
                prod /= nums[left]
                left += 1
            count += right - left + 1
            right += 1

        return count
