class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = {'+', '-', '/', '*'}
        stack = []

        for token in tokens:
            if token in store:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == '+':
                    stack.append(first + second)
                    print(first + second)

                elif token == '-':
                    stack.append(first - second)
                    print(first - second)

                elif token == '*':
                    stack.append(first * second)
                    print(first * second)
                
                else:
                    if first * second < 0:
                        stack.append(-(-first // second))
                    else:
                        stack.append(first // second)
                    print(first // second)


            else:
                stack.append(token)

        return int(stack[0])