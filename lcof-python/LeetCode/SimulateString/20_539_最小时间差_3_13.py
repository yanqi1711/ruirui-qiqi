class Solution:
    def sub(self, str1,str2) -> int:
        result = 0
        str3 = int(str2[0:2]) - int(str1[0:2])
        str4 = int(str2[3:5]) - int(str1[3:5])
        result = str3 * 60 + str4
        if result > 720:
            result -= 1440
            return -result
        return result

    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        print(timePoints)
        length = len(timePoints)
        min_result = self.sub(timePoints[0], timePoints[1])
        for i in range(2,length):
            min_result = min(min_result, self.sub(timePoints[i-1],timePoints[i]))
        # 第一个和最后一个相比  前面都是0
        # 00:00 23:59
        min_result = min(min_result,self.sub(timePoints[0], timePoints[-1]))
        return min_result
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time to minutes
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Check for duplicates 重复的时间点之间的最小差值为0。
        # 如果有重复时间 直接设置为0 快!
        if len(set(timePoints)) < len(timePoints):
            return 0
        
        # Convert times to minutes and sort
        minutes = sorted(time_to_minutes(time) for time in timePoints)
        
        # Calculate minimum difference
        min_diff = float("inf")
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)
        
        # 计算了从最后一个时间点到第一个时间点之间的总分钟数
        circular_diff = (24 * 60 - minutes[-1] + minutes[0]) % (24 * 60)
        min_diff = min(min_diff, circular_diff)
        
        return min_diff