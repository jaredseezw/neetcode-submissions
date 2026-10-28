class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            l = len(stack) - 1
            match c:
                case "}":
                    if stack[l] == "{":
                        stack.pop()
                case ")":
                    if stack[l] == "(":
                        stack.pop()
                case "]":
                    if stack[l] == "[":
                        stack.pop()
                case _:
                    stack.append(c)
        if len(stack) > 0:
            return False
        return True
