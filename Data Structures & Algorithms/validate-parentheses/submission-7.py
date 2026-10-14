class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #When meet corr open at stack, pop
        for c in s:
            if not stack:
                if c in ")]}":
                    return False
                stack.append(c)
                continue
            match c:
                case "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else: 
                        return False
                case "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                case ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                case _: 
                    stack.append(c)
        if len(stack) == 0:
            return True
        return False