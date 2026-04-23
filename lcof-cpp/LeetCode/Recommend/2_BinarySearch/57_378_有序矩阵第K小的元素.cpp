class Solution {
public:
    // 检查有mid左右各有多少个数字
    bool check(vector<vector<int>>& v,int mid, int k)
    {
        // 左下角开始找
        int i = v.size()-1;
        int j = 0;
        int count = 0;
        while(i >= 0 && j<v[0].size())
        {
            if(mid >= v[i][j])
            {
                count+= i+1;
                ++j;
            }
            else
                --i;
        }
        return count >= k;//count个比mid小的
    }

    int kthSmallest(vector<vector<int>>& matrix, int k) {
        // 左下开始
        int minVal=matrix[0][0],maxVal = matrix[matrix.size()-1][matrix[0].size()-1];
        // 都闭合了 也就是说 相等是有效区间，故在左右划分时要-1 +1
        while(minVal <= maxVal)
        {
            int  mid =  (minVal+maxVal)>>1;
            if(check( matrix, mid,k))
                maxVal = mid-1;
            else    
                minVal = mid +1;
        }
        return minVal;
    }
};