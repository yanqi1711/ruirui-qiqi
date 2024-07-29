class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans =[]
        q = deque([root])
        while q:
            layerVal = []
            temp = []
            while q:
                node = q.popleft()
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                layerVal.append(node.val)
            q.extend(temp)
            ans.append(layerVal)
        ans.reverse()
        return ans
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        # append和初始花不一样 初始化给你一个空[] 然后在里面append([])即[[root, 0]]
        q = deque([[root,0]])
        tmp = []
        while(q):
            node,depth = q.popleft()
            if((len(tmp)-1)<depth):
                tmp.append([node.val])
            else:
                tmp[depth].append(node.val)
            if(node.left):
                q.append([node.left,depth+1])
            if(node.right):
                q.append([node.right,depth+1])
        print(tmp)
        return tmp[::-1]