class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = len(tokens)
        
        for i in range(length):
            if len(stack) < 3:
                stack.append(tokens[i])
                
            if len(stack) == 3:
                operation = stack.pop()
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                value = 0
                match operation:
                    case '+':
                        value = value1 + value2
                    case '-':
                        value = value1 - value2
                    case '*':
                        value = value1 * value2
                    case '/':
                        value = value1 / value2
                stack.append(value)

        return stack[0]