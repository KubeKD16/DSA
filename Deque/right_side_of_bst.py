
import collections
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution:
    def rightSideView(self,root: TreeNode):
        deque = collections.deque()
        res = []
        if root:
            deque.append(root)
        
        print(deque)
        while deque:
            size, val = len(deque), 0
            node = deque.popleft()
            print(node)
            # val = node.val
            if node.left:
                deque.append(node.left)
            if node.right:
                deque.append(node.right)
        
        res.append(val)
    
        return res






class Main:
    if __name__ == '__main__':
        x = Solution()
        input = [1,2,3,4]
        obj = x.rightSideView(input)

        print(obj)


