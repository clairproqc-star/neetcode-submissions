class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        max_length = 1
        mySet=set()
        mySet.add(s[l])
        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
                max_length = max(max_length, r - l + 1)
                r += 1
            else:
                mySet.remove(s[l])
                l+=1
        return max_length