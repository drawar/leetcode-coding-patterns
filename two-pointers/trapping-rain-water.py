# We notice that for `n < 3`, the amount of water trapped is 0. In the simplest case where `n = 3`:

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0fef65f2-1d03-4644-ad7e-5de61d385d3b/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0fef65f2-1d03-4644-ad7e-5de61d385d3b/Untitled.png)

# We notice that the amount of water trapped at index i can be calculated as

# `water[i] = min(height[i-1], height[i+1]) - height[i]`

# When `n > 3`, the formula is generalized to

# `water[i] = min(max(height[:i]), max(height[i+1:])) - height[i]`

# From this formula, we can have our brute-force solution, which for each index `i` of the array height, iterates through the two subarrays demarcated by `i` to find the max in each. This takes $O(n^2)$ time overall since we have one $O(n)$ outer loop and two $O(n)$  inner loops. Space complexity is $O(1)$ since we don't use any additional data structures.

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f453dfc-e371-452a-80c8-70ee6682894e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f453dfc-e371-452a-80c8-70ee6682894e/Untitled.png)

# To optimize for time, notice that we can precompute store the results of `max(height[:i])` and `max(height[i+1:])` in two arrays, e.g. `left_max[i]` and `right_max[i]`, respectively, and access them when needed. This way, we cut the time down to $O(n)$ but we have to allocate $O(n)$ space for the arrays. The solution would look like this:

# ```python
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         if len(height) < 3:
#             return 0
#         ans = 0
#         left_max = [0 for i in range(len(height))]
#         right_max = [0 for i in range(len(height))]
#         left_max[0] = height[0]
#         right_max[-1] = height[-1]
#         for i in range(1, len(height)):
#             left_max[i] = max(left_max[i-1], height[i])
#         for i in range(len(height) - 2, -1, -1):
#             right_max[i] = max(right_max[i+1], height[i])
#         for i in range(len(height)):
#             ans += min(left_max[i], right_max[i]) - height[i]
#         return ans
# ```

# This is good, but there's still room for improvement. The main hurdle of the problem we're trying to solve is this mini problem

# > Given `H[1..n]`, calculate the function `g(i) := min(max(H[1..i]), max(H[i..n]))` for `i = 1, 2,.., n`.

# To plot `g(i)`, we first plot `max(H[1..i])` i.e. `left_max` in purple and `max(H[i..n])` i.e. `right_max` in blue.

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab085b45-78a2-4078-9c84-a22f536dbd93/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ab085b45-78a2-4078-9c84-a22f536dbd93/Untitled.png)

# If we take the `min` of these two, we will get `g(i)`, which is also called the *lower envelope* of `left_max` and `right_max`. Our goal is to be able to calculate `g(i)` without using `left_max` and `right_max` explicitly, because that would be the same as the DP solution. But if we can't use each element of `left_max` and `right_max` explicitly, how can we calculate `g(i)`?

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8624b0c2-115e-44ea-9269-3fccf1dda930/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8624b0c2-115e-44ea-9269-3fccf1dda930/Untitled.png)

# Turns out we can take advantage of the monotonicity property of the lower envelope. Notice that the envelope is a combination of a non-decreasing function (in purple - from `left_max`) and a non-increasing function (in blue - from `right_max`). Using this property, we can compute `g(i)` without using all values of `left_max` and `right_max`. Here we attempt to calculate `g(10)` using only `left_max[1]` and `right_max[10]`.

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b58cc3c3-7152-4620-a502-9d9ac2933f54/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b58cc3c3-7152-4620-a502-9d9ac2933f54/Untitled.png)

# Since left_max is non-decreasing and `left_max[1] = 1`, `left_max[10]` must be at least 1, but we know `right_max[10] = 0`, so although we don't know exactly what `left_max[10]` is, we are certain that `g(10) = 0`.

# However, we can't reach the same conclusion about `g(1)`, as by the time right_max is at index 1, it is definitely greater than or equal to 0 but might be above or below 1, we don't know which. Hence we continue in the direction of index 10, by decrementing `j`. We repeat the process by alternating between incrementing `i` and decrementing `j`

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9eb721e6-f9e5-439d-bcf0-31780315e74a/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9eb721e6-f9e5-439d-bcf0-31780315e74a/Untitled.png)

# When `left_max[i]` and `right_max[j]` are the same, it doesn't matter which pointer gets to move, but we can only move one. When `i` meets `j`, we are done.

# ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3d94bdc-77fe-4bc5-a7d1-096269169190/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a3d94bdc-77fe-4bc5-a7d1-096269169190/Untitled.png)

# The complete code is as follows

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        ans = 0
        left, right = 0, len(height) - 1
        left_max = right_max = -1
        while i <= right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max > right_max:
                ans += right_max - height[right]
                right -= 1
            else:
                ans += left_max - height[left]
                left += 1
        return ans

# Time complexity: $O(n)$ where $n$ is the length of `height`. Each pointer (left and right) only traverse at most $n$ steps.
# Space complexity: $O(1)$. Constant space for `left`, `right`, `left_max`, `right_max`.
