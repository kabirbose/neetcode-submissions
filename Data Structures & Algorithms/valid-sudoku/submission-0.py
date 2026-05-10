class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(len(board)):
            duplicates = set()
            
            for j in range(len(board)):
                row = board[i]
                val = board[i][j]
                
                if val in duplicates:
                    return False
                
                if val in row and val not in duplicates and val != ".":
                    duplicates.add(val)
        
        # check columns
        for i in range(len(board)):
            duplicates = set()
            
            for j in range(len(board)):
                col = board[j]
                val = board[j][i]
                
                if val in duplicates:
                    return False
                
                if val in col and val not in duplicates and val != ".":
                    duplicates.add(val)
        
        # check grids
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6),
        ]

        for i, j in starts:
            duplicates = set()
            
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    item = board[row][col]
                    
                    if item in duplicates:
                        return False
                    
                    if item != '.' and item not in duplicates:
                        duplicates.add(item)

        return True

'''
Some iterations for grid check

row: 0 col: 0 item: 1, dups: {'1'}
row: 0 col: 1 item: 2, dups: {'2', '1'}
row: 0 col: 2 item: ., dups: {'2', '1'}
row: 1 col: 0 item: 4, dups: {'2', '1', '4'}
row: 1 col: 1 item: ., dups: {'2', '1', '4'}
row: 1 col: 2 item: ., dups: {'2', '1', '4'}
row: 2 col: 0 item: ., dups: {'2', '1', '4'}
row: 2 col: 1 item: 9, dups: {'2', '1', '9', '4'}
row: 2 col: 2 item: 8, dups: {'2', '4', '1', '9', '8'}

row: 0 col: 3 item: ., dups: set()
row: 0 col: 4 item: 3, dups: {'3'}
row: 0 col: 5 item: ., dups: {'3'}
row: 1 col: 3 item: 5, dups: {'5', '3'}
row: 1 col: 4 item: ., dups: {'5', '3'}
row: 1 col: 5 item: ., dups: {'5', '3'}
row: 2 col: 3 item: ., dups: {'5', '3'}
row: 2 col: 4 item: ., dups: {'5', '3'}
row: 2 col: 5 item: ., dups: {'5', '3'}
'''



