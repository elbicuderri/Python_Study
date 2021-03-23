# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
        
def return_left_val(node):
    
    left_node = node.left
    if left_node is None:
        return node.val
    
    else:
        while left_node is not None:
            left_val = left_node.val
            left_node = left_node.left
            
    return left_val
    
def return_leaf_seq(node):
    leaf_seq = []
    return None
    

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        # root1_val = root1.left.val
        root1_left_node = root1.left
        if root1_left_node is None:
            return False
        
        else:
            while root1_left_node is not None:
                root1_val = root1_left_node.val
                root1_left_node = root1_left_node.left
                
                
# TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None},
# right: TreeNode{val: 2, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 4, left: None, right: None}}}, right: TreeNode{val: 1, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}
# ////
# TreeNode{val: 3, left: TreeNode{val: 5, left: TreeNode{val: 6, left: None, right: None},
# right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 1, left: TreeNode{val: 4, left: None, right: None}, right: TreeNode{val: 2, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 8, left: None, right: None}}}}