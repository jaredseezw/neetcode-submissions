class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #When meet corr open at stack, pop
        for c in s:
            if len(stack) == 0:
                stack.append(c)
                continue;
            match c:
                case "}":
                    if stack[-1] == "{":
                        stack.pop()
                    return False 
                case "]":
                    if stack[-1] == "[":
                        stack.pop()
                    return False
                case ")":
                    if stack[-1] == "(":
                        stack.pop()
                    return False
                case _: 
                    stack.append(c)
        if len(stack) == 0:
            return True
        return False