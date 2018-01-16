class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


# inorder
def inorder_traverse_recursive_util(node, res):
    if not node:
        return
    inorder_traverse_recursive_util(node.left, res)
    res.append(node.val)
    inorder_traverse_recursive_util(node.right, res)


def inorder_traverse_recursive(root):
    if not root:
        return []
    res = []
    inorder_traverse_recursive_util(root, res)
    return res
print(inorder_traverse_recursive(root))

def inorder_traverse(root):
    if not root:
        return []
    res = []
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            res.append(root.val)
            root = root.right
    return res

print(inorder_traverse(root))


# preorder

def preorder_traverse_recursive_util(node, res):
    if not node:
        return
    res.append(node.val)
    preorder_traverse_recursive_util(node.left, res)
    preorder_traverse_recursive_util(node.right, res)

def preorder_traverse_recursive(root):
    if not root:
        return []
    res = []
    preorder_traverse_recursive_util(root, res)
    return res
print(preorder_traverse_recursive(root))

def preorder_traverse(root):
    if not root:
        return []
    res = []
    stack = []
    while stack or root:
        if root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root = root.right
    return res
print(preorder_traverse(root))


# postorder
def postorder_traverse_recursive_util(node, res):
    if not node:
        return
    postorder_traverse_recursive_util(node.left, res)
    postorder_traverse_recursive_util(node.right, res)
    res.append(node.val)


def postorder_traverse_recursive(root):
    if not root:
        return []
    res = []
    postorder_traverse_recursive_util(root, res)
    return res
print(postorder_traverse_recursive(root))


def postOrder(root):
    res = []
    stack = []
    preNode = None
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            peekNode = stack[-1]
            if peekNode.right and preNode != peekNode.right:
                root = peekNode.right
            else:
                stack.pop()
                res.append(peekNode.val)
                preNode = peekNode
    return res
print(postOrder(root))


