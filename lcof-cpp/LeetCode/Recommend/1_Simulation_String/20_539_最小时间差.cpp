class Solution {
public:
    int parseMinutes(string & timePoints)
    {
        int hours = std::stoi(timePoints.substr(0, 2));
        int minutes = std::stoi(timePoints.substr(3, 2));
        int totalMinutes = hours * 60 + minutes;
    
        return totalMinutes;
    }
    int findMinDifference(vector<string>& timePoints) {
        const int TOTAL_MINUTES = 1440; // 24*60
        vector<bool> bucket(TOTAL_MINUTES, false);
        
        // 填充桶并检查重复
        for (auto& time : timePoints) {
            int minutes = parseMinutes(time);
            if (bucket[minutes]) return 0; // 发现重复时间点
            bucket[minutes] = true;
        }
        
        int min_diff = INT_MAX;
        int prev = -1;
        int first = -1;
        int last = -1;
        
        // 遍历桶寻找最小差值
        for (int i = 0; i < TOTAL_MINUTES; ++i) {
            if (!bucket[i]) continue;
            
            if (prev == -1) {
                first = i; // 记录第一个时间点
            } else {
                min_diff = min(min_diff, i - prev); // 更新相邻时间差
            }
            
            last = i; // 更新最后一个时间点
            prev = i; // 更新前一个有效时间点
        }
        
        // 检查首尾循环时间差
        min_diff = min(min_diff, first + TOTAL_MINUTES - last);
        return min_diff;
    }
};