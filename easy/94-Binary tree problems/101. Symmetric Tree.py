#Logic (DFS)
def isTreeSymmetric(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return self.isTreeSymmetric(leftRoot.left, rightRoot.right) and self.isTreeSymmetric(leftRoot.right, rightRoot.left)
def isSymmetric(self, root):
    return self.isTreeSymmetric(root.left, root.right)
