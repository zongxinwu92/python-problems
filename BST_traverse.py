class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


# if want to traverse BST in increasing order, use the inorder traverse:


def increading_BST_traverse(root):
    if not root:
        return []
    res = []
    increading_BST_traverse_util(root, res)
    return res


def increading_BST_traverse_util(node, res):
    if not node:
        return
    increading_BST_traverse_util(node.left, res)
    res.append(node.val)
    increading_BST_traverse_util(node.right, res)

print(increading_BST_traverse(root))


def descending_BST_traverse(root):
    if not root:
        return []
    res = []
    descending_BST_traverse_util(root, res)
    return res


def descending_BST_traverse_util(node, res):
    if not node:
        return
    descending_BST_traverse_util(node.right, res)
    res.append(node.val)
    descending_BST_traverse_util(node.left, res)

print(descending_BST_traverse(root))

