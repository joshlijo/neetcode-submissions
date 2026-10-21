class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1          # two pointers at the ends
        while L < R:                   # stop when they cross
            # move L right until it points at an alphanumeric
            while L < R and not s[L].isalnum():
                L += 1
            # move R left until it points at an alphanumeric
            while L < R and not s[R].isalnum():
                R -= 1

            # compare case-insensitively
            if s[L].casefold() != s[R].casefold():
                return False           # mismatch → not a palindrome

            # move inward for the next pair
            L += 1
            R -= 1

        return True                    # all pairs matched