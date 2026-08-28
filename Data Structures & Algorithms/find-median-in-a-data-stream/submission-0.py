class MedianFinder:

    def __init__(self):
        self.small,self.large=[],[]

    def addNum(self, num: int) -> None:
        # check if the num is bigger than min of large
        if len(self.large)>0 and num>self.large[0]:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-1*num)
        
        # check if the length of heaps
        if len(self.small)>len(self.large)+1:
            heapq.heappush(self.large,-1*heapq.heappop(self.small))
        if len(self.large)>len(self.small)+1:
            heapq.heappush(self.small,-1*heapq.heappop(self.large))



    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-1*(self.small[0])+(self.large[0]))/2
        elif len(self.small)==len(self.large)+1:
            return -1*(self.small[0])
        else:
            return self.large[0]

        
        