class Solution:
    def isValid(self, s: str) -> bool:
        answerMap={
            ")":"(",
            "}":"{",
            "]":"["
        }
        window=[]
        for r in range(len(s)):
            if len(window)>0 :
                print(window,s[r])
                if answerMap.get(s[r],0):
                    if window[-1]==answerMap[s[r]]:
                        window.pop()
                    else:
                        return False
                else:
                    window.append(s[r])

            else:
                window.append(s[r])
        return len(window)==0    

        