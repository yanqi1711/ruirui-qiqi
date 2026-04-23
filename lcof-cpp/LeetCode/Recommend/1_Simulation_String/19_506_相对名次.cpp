class Solution {
public:
    vector<string> findRelativeRanks(vector<int>& score) {
        vector<pair<int, int>> score2index;
        string desc[3] = {"Gold Medal", "Silver Medal", "Bronze Medal"};
        for(int i=0; i<score.size(); ++i)
            score2index.emplace_back(-score[i], i);
        sort(score2index.begin(), score2index.end());
        vector<string> ans(score.size());
        for(int i=0;i<score.size();++i)
        {
            if(i>=3)
                ans[score2index[i].second] =to_string(i+1);
            else
                ans[score2index[i].second] =desc[i];
        }
        return ans;
    }
};