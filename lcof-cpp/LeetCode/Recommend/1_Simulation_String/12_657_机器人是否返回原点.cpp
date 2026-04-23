class Solution {
public:
    bool judgeCircle(string moves) {
        int vertical = 0;
        int horizontal = 0;
        for(auto ch:moves)
        {
            switch (ch)
            {
            case 'U':
                vertical+=1;
                break;
            case 'D':
                vertical-=1;
                break;            
            case 'L':
                horizontal-=1;
                break;            
            case 'R':
                horizontal+=1;
                break;
            default:
                break;
            } 
        }
        return vertical == 0 && horizontal ==0;
    }
};