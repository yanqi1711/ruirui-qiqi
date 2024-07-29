class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contenToPath = {}
        for i in paths:
            start = True
            for j in i.split():
                if start:
                    path = j
                    start = False
                    continue
                index = j.find('(')
                if j[index+1:-1] in contenToPath:
                    contenToPath[j[index+1 : -1]].append(path+'/' + j[:index])
                else:
                    contenToPath[j[index+1:-1]] = [path +'/'+ j[:index]]
        print(contenToPath)
        ans = []
        for j in contenToPath.values():
            print(j)
            if len(j) >= 2:
                ans.append(j)
        return ans