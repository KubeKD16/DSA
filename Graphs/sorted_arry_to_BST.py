"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

 

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in a strictly increasing order.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}".format(self.val)

class Graph:
    def sortedarrayToBST(self,nums):
        if len(nums) == 0:
            return None
        
        mid = len(nums)//2
        root = nums[mid]
        root_node = TreeNode(root)
        preOrder(root_node)
        root_node_left = self.sortedarrayToBST(nums[:mid])
        root_node_right = self.sortedarrayToBST(nums[mid+1:])

        return root_node

def preOrder(s):
    if not s:
        return None
    
    print(s.val)
    preOrder(s.left)
    preOrder(s.right)




g = Graph()
n = [-10, -3, 0, 5, 9]
g.sortedarrayToBST(n)
