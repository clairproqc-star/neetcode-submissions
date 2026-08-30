class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(start:int,remain:int,path:list[int]):
            if remain==0:
                res.append(list(path))
                return
            if remain<0:
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i,remain-nums[i],path)
                path.pop()
            
        backtrack(0,target,[])
        return res