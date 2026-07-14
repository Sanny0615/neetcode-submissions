class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        # Sort the dictionary keys based on their frequency (values)
        # and take the first k elements.
        l = sorted(d, key=d.get, reverse=True)[:k]
        return l