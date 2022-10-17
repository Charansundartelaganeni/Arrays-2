#TC: O(m*n)
#SC: O(1)


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board) 
        n = len(board[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]] 
        
        
        #first traversal 
        
        for i in range(m): 
            for j in range(n): 
                count = 0 
                
                for r,c in dirs: #traversing through the direction array
                    
                    nr = r+i 
                    nc = c+j 
                    
                    if nr>=0 and nr<m and nc>=0 and nc<n:  #checking the edge cases
                        if board[nr][nc] == -1 or board[nr][nc] == 1: 
                            count+=1 
                            
                if board[i][j] == 1: #changing the values of the items as -1 if they are going to die
                    if count<2 or count >3: 
                        board[i][j] = -1 
                        
                else: 
                    if count == 3:  #changing the values of the items as 2 if they are going to be alive from dead
                        board[i][j] = 2 
                        
        
        for i in range(m): 
            for j in range(n): 
                if board[i][j] == -1: #now change the dead to 0
                    board[i][j] = 0 
                    
                elif board[i][j] == 2: #now change the dead to 1
                    board[i][j] = 1