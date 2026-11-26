class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        operators = []
        allowed_opers = set(['+','-','*','/'])
        for token in tokens:
            if token not in allowed_opers:
                nums.append(int(token))
            else:
                right, left = nums.pop(), nums.pop()
                print(left, right)
                if token == '+':
                    nums.append(left + right)
                elif token == '-':
                    nums.append(left - right)
                elif token == '*':
                    nums.append(left * right)
                else:
                    nums.append(int(left / right))
        return nums[-1]