class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def check_row(board: List[List[str]]) -> bool:
            m, n = len(board), len(board[0])
            for i in range(m):
                cur_dict = collections.defaultdict(int)
                for j in range(n):
                    item = board[i][j]
                    if item != '.':
                        cur_dict[item] += 1
                        if cur_dict[item] > 1:
                            return False
            return True

        def check_column(board: List[List[str]]) -> bool:
            m, n = len(board), len(board[0])
            for j in range(n):
                cur_dict = collections.defaultdict(int)
                for i in range(m):
                    item = board[i][j]
                    if item != '.':
                        cur_dict[item] += 1
                        if cur_dict[item] > 1:
                            return False
            return True
        
        def check_square(board: List[List[str]]) -> bool:
            for i in range(0,9,3):
                for j in range(0,9,3):
                    cur_dict = collections.defaultdict(int)
                    for m in range(3):
                        for n in range(3):
                            item = board[i+m][j+n]
                            if item != '.':
                                cur_dict[item] += 1
                                if cur_dict[item] > 1:
                                    return False
            return True
        a = check_row(board) 
        b = check_column(board)
        c = check_square(board)

        return a and b and c

