class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        path = []
        ans = []
        def backtrack(start):
            print(path)
            if len(path) == n:
                ans.append(path.copy())
                return
            banned = set()
            for i in range(len(path)):
                banned.add(path[i])
                banned.add(path[i] + (start - i))
                banned.add(path[i] - (start - i))
            # print(start,banned,path)
            for i in range(n):
                if i not in banned:
                    path.append(i)
                    backtrack(start+1)
                    path.pop()

        backtrack(0)
        final_ans = []
        for path in ans:
            cur = []
            for i in path:
                s = ['.'] * n
                s[i] = "Q"
                cur.append(''.join(s))
            final_ans.append(cur)
        return final_ans

