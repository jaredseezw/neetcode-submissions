class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        length = len(tokens)
        
        for i in range(length):    
            if tokens[i] in ['+', '*', '/', '-']:
                operation = tokens[i]
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
            else:
                stack.append(tokens[i])

        return stack[0]