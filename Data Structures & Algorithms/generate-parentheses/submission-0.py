class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(path,left,right):
            print(path,left,right)
            if left == right == n:
                ans.append("".join(path))
            elif right <= left:
                if left < n:
                    path.append('(')
                    backtrack(path,left+1,right)
                    path.pop()
                if right < left:
                    path.append(')')
                    backtrack(path,left,right+1)
                    path.pop()
        path = []
        backtrack(path,0,0)
        return ans


