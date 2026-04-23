class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # 存储的是前序遍历每一次的结果,因为需要回溯 比如根目录是需要重复使用 
        st = [] 
        # input符合树的前序遍历 ans是最后结果记录时文件的返回值，当没有文件的时候返回0
        ans,i, n = 0,0,len(input)
        # 开始遍历 如果时子文件夹会有多个连续的\t
        while i < n:
            depth=1
            # 检测深度也就是现在在树的第几层
            while i<n and input[i] == "\t":
                depth+=1
                i+=1
            
            # 统计当前文件名长度
            length, isFile = 0, False
            while i < n and input[i] != '\n':
                if input[i] == '.':
                    isFile = True
                length += 1
                i += 1
            i+=1 #换行符
            while len(st) >= depth:
                # 多次判断来回溯 因为depth深度根据\t判断 如果是同一个深度就是等于 需要重新计算长度
                # 如果是 > 的情况说明当前文件夹最后一个都遍历完，需要进入父文件夹去遍历父文件夹的下一个文件
                st.pop()
            if st: #判断是否存在元素 +1是/
                length += st[-1] +1
            if isFile:
                ans = max(ans, length)
            else:
                st.append(length)
        return ans