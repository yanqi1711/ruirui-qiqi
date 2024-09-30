class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        length = len(score)
        if length == 1:
            return ["Gold Medal"]
        hash = {}
        for i in range(length):
            hash[i] = score[i]
        hash = dict(sorted(hash.items(),key = lambda x:x[1],reverse = True))
        result = [0]*length
        count = 1
        temp = []
        for key,value in hash.items():
            if count <=3:
                temp.append(key)
            result[key] = str(count)
            count += 1
        t = 1
        for j in temp:
            if t == 1:
                result[j] = "Gold Medal"
            elif t == 2:
                result[j] = "Silver Medal"
            else:
                result[j] = "Bronze Medal"
            t+=1
        return result
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        hash={}
        res=[None]*len(score)
        # 利用分数记录 索引
        for i in range(len(score)):
            hash[score[i]]=i
        # 排序
        score.sort(reverse=True)
        # 最高分最前面
        for i in range(len(score)):
            if i==0:
                # 直接利用最高分找到期本来索引 然后把原来的分数改为名次
                res[hash[score[i]]]="Gold Medal"
            elif i==1:
                res[hash[score[i]]]="Silver Medal"
            elif i==2:
                res[hash[score[i]]]="Bronze Medal"
            else:
                res[hash[score[i]]]="%d"%(i+1)
        return res