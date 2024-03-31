#Logic
def main(root):
    return 1+max(main(root.left), main(root.right)) if root else 0
