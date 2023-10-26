class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = {'+','-', '*', '/'}

        for operand in tokens:
            if operand not in operands:
                stack.append(operand)

            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if operand == '+':
                    stack.append(int(left + right))
                elif operand == '-':
                    stack.append(int(left - right))
                elif operand == '*':
                    stack.append(int(left * right) )
                elif operand == '/':
                    stack.append(int(left / right) )
        return int(stack[0])