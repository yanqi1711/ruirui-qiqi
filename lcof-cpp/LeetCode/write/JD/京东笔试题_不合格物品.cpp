#include <bits/stdc++.h>
#include <iostream>
using namespace std;
struct Goods
{
    Goods(int x, int y, int z) : x(x), y(y), z(z)
    {
    }
    bool operator<(const Goods &other)
    {
        if (x < other.x && y < other.y && z < other.z)
            return true;
        else
            return false;
    }
    int x;
    int y;
    int z;
};
int main()
{
    int n;
    cin >> n;
    vector<Goods> vGoods;
    int a, b, c;
    int res = 0;
    while (n--)
    {
        cin >> a >> b >> c;
        vGoods.emplace_back(a, b, c);
    }
    for (int i = 0; i < vGoods.size() - 1; ++i)
    {
        cout << "index=" << i << "\n";
        for (int j = i + 1; j < vGoods.size(); ++j)
        {
            if (vGoods[i] < vGoods[j])
            {
                cout << "i=" << i << ",j=" << j << "\n";
                ++res;
                break;
            }
        }
    }
    cout << res << "\n";
    return res;
}