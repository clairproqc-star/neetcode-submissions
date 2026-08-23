class Solution:
    def isValid(self, s: str) -> bool:
        answerMap={
            ")":"(",
            "}":"{",
            "]":"["
        }
        window=[]
        for r in range(len(s)):
            if len(window)>0 and answerMap.get(s[r],0)==window[-1]:
                window.pop()
            else:
                window.append(s[r])
        return len(window)==0  