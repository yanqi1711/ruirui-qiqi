/*
https://www.nowcoder.com/exam/test/92327940/detail?pid=62071763&examPageSource=Company&subTabName=written_page&testCallback=https%3A%2F%2Fwww.nowcoder.com%2Fexam%2Fcompany%3FcurrentTab%3Drecommand%26jobId%3D100%26tagIds%3D151&testclass=%E8%BD%AF%E4%BB%B6%E5%BC%80%E5%8F%91
*/

#include <complex>
#include <ios>
#include <iostream>
#include <numeric>
#include <utility>
#include <vector>
using namespace std;

int main()
{
    vector<long long> v;
    int n;
    cin >> n;
    while (n--)
    {
        int m;
        cin >> m;
        v.emplace_back(m);
    }
    long long s = std::accumulate(v.begin(), v.end(), 0);
    // std::cout << s << "==\n";
    long long lSum = v[0];
    long long rSum = s - lSum;
    long long maxDiff = -2147483648;
    pair<long long, long long> p(maxDiff, 0);
    for (int i = 1; i < v.size(); ++i)
    {
        long long diff = abs(rSum - lSum);

        if (diff > maxDiff)
        {
            // cout << diff << '=' << i<< '\n';
            maxDiff = diff;
            p.first = diff;
            p.second = i;
        }
        rSum -= v[i];
        lSum += v[i];
    }
    long long l = std::accumulate(v.begin(), v.begin() + p.second, 0);
    long long r = std::accumulate(v.begin() + p.second, v.end(), 0);
    // cout << "p.first="<<p.first <<" p.second="<< p.second << endl;
    // cout << "l="<<l <<" r="<< r << endl;
    cout << l * r << endl;
    ;
    return 0;
}
// 64 位输出请用 printf("%lld")