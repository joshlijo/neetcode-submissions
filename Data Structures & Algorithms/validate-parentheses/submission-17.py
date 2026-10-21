class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for element in s:
            if element in "({[":
                stack.append(element)
            elif element in ")}]":
                if not stack:
                    return False
                else:
                    top = stack.pop()

                if top != pairs[element]:
                    return False

        return not stack