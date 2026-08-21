
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product
        prefix = [1] 
        for i in range(1, len(nums)):
            prefix.append(prefix[i - 1] * nums[i - 1])


        # postfix product
        res=[1]*len(nums)
        res[(len(nums) - 1)] = prefix[(len(nums) - 1)]
        postfix =1

        for i in range(len(nums) - 2, -1, -1):
            postfix=postfix* nums[i + 1]
            res[i] = prefix[i] * postfix
        return res
