class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islandCount=0
        rows,columns=len(grid),len(grid[0])
        
        def dfs(r,c):
            if  r<0 or c<0 or r>=rows or c>=columns or grid[r][c]=='0':
                return
            grid[r][c]='0'

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)


        for r in range(rows):
            for c in range(columns):
                if grid[r][c]=='1':
                    islandCount+=1
                    dfs(r,c)
        return islandCount
