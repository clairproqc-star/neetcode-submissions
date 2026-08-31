class TrieNode:
    def __init__(self):
        self.children={}
        self.endOfWord=False
    def addWord(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endOfWord=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # create TrieNode
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS,COLUMNS=len(board),len(board[0])
        res,visited=set(),set()

        def dfs(r,c,node,word):
            
            if r>=ROWS or c>=COLUMNS or (r,c) in visited or board[r][c] not in node.children or r<0 or c<0:
                return
            visited.add((r,c))
            word+=board[r][c]
            node=node.children[board[r][c]]
            if node.endOfWord:
                res.add(word)
             
            dfs(r+1,c,node,word) 
            dfs(r-1,c,node,word) 
            dfs(r,c-1,node,word) 
            dfs(r,c+1,node,word)

            visited.remove((r,c))
                    

        # loop through the board
        for r in range(ROWS):
            for c in range(COLUMNS):
                dfs(r,c,root,'')
        return list(res)