class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            l = len(stack)
            if l == 0:
                stack.append(c)
            match c:
                case "}":
                    if stack[-1] == "{":
                        stack.pop()
                case ")":
                    if stack[-1] == "(":
                        stack.pop()
                case "]":
                    if stack[-1] == "[":
                        stack.pop()
                case _:
                    stack.append(c)
        if len(stack) > 0:
            return False
        return True
