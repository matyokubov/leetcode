#Input
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
p = TreeNode(1, right=TreeNode(1))
q = TreeNode(1, right=TreeNode(1, left=TreeNode(None)))

#Logic
def main(p, q):
    '''Deep First Search algorithm - DFS'''
    # If p and q are both None, return True.
    # Because it's technicialy True: None=None
    if not p and not q:
        return True
    # Otherwise, one of p and q isn't None.
    # So, if they aren't equal, return False
    if not p or not q or p.val != q.val:
        return False
    # If the above conditions don't work, then we have equal values (q=p)
    # We do the recursion until the first condition returns True (None=None)
    # Because it's "the end"
    return main(p.left, q.left) and main(p.right, q.right)
    
#Output
print(main(p, q))

