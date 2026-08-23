class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        countMap={}
        l=0
        maxCount=0
        for r in range(len(s)):
            countMap[s[r]]=countMap.get(s[r],0)+1
            maxCount=max(maxCount,countMap[s[r]])
            if (r-l+1)-maxCount>k:
                countMap[s[l]]-=1
                l+=1
        return min(maxCount+k, len(s))