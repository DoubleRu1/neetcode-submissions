class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_dict = {0:['+'],1:[],2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        ans = []

        def backtrack(path,idx):
            if len(path) == len(digits):
                if path != "":
                    ans.append(path)
                return
            for ch in digit_dict[int(digits[idx])]:
                backtrack(path+ch,idx+1)
        backtrack("",0)
        return ans
