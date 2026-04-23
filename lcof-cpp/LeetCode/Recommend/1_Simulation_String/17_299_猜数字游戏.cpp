class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> S(10,0),G(10,0);//记录的是2个数组不同的部分,一个有一个没有 那就取0->说明压根没匹配上
        int A = 0;
        for(int i=0;i<secret.size(); ++i)
        {
            if(secret[i] == guess[i])
            {
                A+=1;
                continue;
            }
            S[secret[i] -'0']+=1;
            G[guess[i] - '0']+=1;
        }
        int B = 0;
        for(int i=0;i<10;++i)
        {   
            B+= std::min(S[i], G[i]);
        }
        return to_string(A) + 'A' + to_string(B) + 'B';
    }
};