class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1
        l=0
        have=0
        haveMap={}
        need=len(tMap)
        res=[-1, -1]
        for r in range(len(s)):
            if tMap.get(s[r],0)>0:
                haveMap[s[r]]=haveMap.get(s[r],0)+1
                if haveMap[s[r]]==tMap[s[r]]:
                    have+=1
                    while have==need:
                        if r-l<res[1]-res[0] or res[0]==-1:
                            res=[l, r]
                        if tMap.get(s[l],0)>0:
                            haveMap[s[l]]-=1
                            if haveMap[s[l]]<tMap[s[l]]:
                                have-=1
                        l+=1
        return "" if res[0]==-1 else s[res[0]:res[1]+1]
                    