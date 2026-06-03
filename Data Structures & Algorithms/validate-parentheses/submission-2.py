class Solution:
    def isValid(self, s: str) -> bool:
        dicta = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            try:
                if stack[-1] == dicta[i]:
                    stack.pop()
                else:
                    return False
            except:
                stack.append(i)
        if len(stack)>0:
            return False
        return True
