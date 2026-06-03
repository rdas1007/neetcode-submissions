class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tot = 0
        for i in tokens:
            if i in ['+', '-', '*', '/']:
                y = stack.pop()
                x = stack.pop()
                exp = str(x) + i + str(y)
                print(exp)
                res = eval(exp)
                stack.append(int(res))
            else:
                stack.append(int(i))
        return stack[-1]