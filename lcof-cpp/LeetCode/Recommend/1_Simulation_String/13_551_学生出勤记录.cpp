class Solution {
public:
    bool checkRecord(string s) {
        int total = 0;
        int late = 0;
        for(auto ch:s)
        {
            if(ch== 'A')
            {
                ++total;
                late = 0;
                if(total >=2)
                    return false;
            }   
            else if(ch == 'L')
            {
                ++late;
                if(late == 3)
                    return false;
            }
            else
                late = 0;
        }
        return true;
    }
};