class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key] = self.dict.get(key,[])
        self.dict[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        timestamps = [item[0] for item in self.dict.get(key,[])]
        left, right = 0, len(timestamps)-1
        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid] == timestamp:
                return self.dict[key][mid][1]
            elif timestamps[mid] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
            
        print(key,left,self.dict)
        if left >= len(self.dict.get(key,[])):
            left = left - 1
        elif self.dict[key][left][0] > timestamp:
            left = left - 1
        if left < 0:
            return ""        
        
        return self.dict[key][left][1]

