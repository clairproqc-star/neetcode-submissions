class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count the frequency of each element in nums
        frequency_map = {}
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1

        # 2. Create a list of buckets where index represents frequency
        buckets =[]
        for i in range(len(nums) + 1):
            buckets.append([])

        # get map pairs
        for num, freq in frequency_map.items():
            buckets[freq].append(num)

        # Collect the top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                result.append(number)
                if len(result) >= k:
                    return result
