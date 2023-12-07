class Solution:
    def FindNumsAppearOnce(self , nums: List[int]) -> List[int]:
        res = [0,0]
        sum = 0
        # 得到 a^b
        for i in nums:
            sum ^= i
        k = 1
        # 找到第一位不一样的数 分组
        while k & sum == 0:
            k <<= 1
        for i in nums:
            # 因为异或必定有一位不一样 所以用这个来区分 一样的数分到的组也是同样的 故其数照样为0
            if k & i == 0:
                res[0] ^= i
            else:
                res[1] ^= i
        return sorted(res)

        # 哈希
        # hashtable = dict()
        # for i in nums:
        #     if i in hashtable.keys():
        #         hashtable[i] += 1
        #         continue
        #     hashtable[i] = 1
        # a = []
        # for key,value in hashtable.items():
        #     if value == 1:
        #         a.append(key)
        # print(hashtable)
        # return sorted(a)