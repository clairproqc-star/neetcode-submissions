class Solution:
    def isValid(self, s: str) -> bool:
        answerMap={
            ")":"(",
            "}":"{",
            "]":"["
        }
        l=0
        window=[]
        for r in range(len(s)):
            if r>l and answerMap.get(s[r],0)==window[-1]:
                print('yes')
                window.pop()
                if len(window)==0:
                    l=r+1
                else:
                    l-=1
            else:
                window.append(s[r])
        return len(window)==0    


        