class Solution {
public:
    string optimalDivision(vector<int>& nums) {
        if(nums.size() <2) return to_string(nums[0]);
        if(nums.size() == 2) return to_string(nums[0])+"/"+to_string(nums[1]);
        string res;
        res.append(to_string(nums[0]));
        res.append("/(");
        for(int i=1; i<nums.size()-1;++i)
        {
          res.append(to_string(nums[i]));
          res.append("/");
        }
        res.append(to_string(nums[nums.size()-1]));
        res.append(")");
        return res;
    }
};