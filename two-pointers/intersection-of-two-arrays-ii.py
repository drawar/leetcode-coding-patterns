# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, k = 0, 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # write result to nums1
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        return nums1[:k]

# Time complexity: $O(M\mathrm{log}M) + O(N\mathrm{log}N) + O(M+N)$  where `M = len(nums1)` and `N = len(nums2)`,
# which is asymptotically equivalent to $O(M\mathrm{log}M + N\mathrm{log}N)$.
# Space complexity: $O(1)$ if we use heap sort or $O(N)$ if we use merge sort.
