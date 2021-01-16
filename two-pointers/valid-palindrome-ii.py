# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# Time complexity: $O(N)$ where N is the length of the string. Each of the two checks of whether the substring is
# a palindrome or not (`isPalindrome(s, left + 1, right)` and `isPalindrome(s, left, right - 1)`)  is $O(N)$
# and although there's a while loop, the check is only performed once cause it only appears in the `return` function.
# Space complexity: $O(1)$. We only keep track of the two pointers.
