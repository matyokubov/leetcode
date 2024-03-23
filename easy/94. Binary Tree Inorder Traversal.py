#Input
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
child3 = TreeNode(val=3)
child1 = TreeNode(val=2, left=child3)
root = TreeNode(val=1, right=child1)

#Logic
def main(root):
    res, stack = [], []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
    
print(main(root))
