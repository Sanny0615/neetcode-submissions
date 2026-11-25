class TimeMap:

    def __init__(self):

        self.timemap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key]=[]
        t=(timestamp,value)
        self.timemap[key].append(t)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap.keys():
            return ""
        ans=""
        t=self.timemap[key]
        start=0
        end=len(t)-1
        while start <= end:
            mid=(start+end)//2
            if t[mid][0]<=timestamp:
                ans=t[mid][1]
                start=mid+1
            else:
                end=mid-1
        return ans

