class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
# 455. Assign Cookies
# this is a greedy problem,
def assign_cookies(g, s):
    new_g = sorted(g)
    new_s = sorted(s)
    count, indexg, indexs = 0, 0, 0
    while indexg < len(g) and indexs < len(s):
        if new_g[indexg] <= new_s[indexs]:
            indexg += 1
            indexs += 1
            count += 1
        else:
            indexs += 1
    return count

# jump game
# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.

# 55. Jump Game.
# Determine if you are able to reach the last index.
def canJump(nums):
    if not nums:
        return True
    goal = len(nums) -1
    cur = 0
    for index,num in enumerate(nums):
        if cur <= index:
            cur = max(cur, index + num)
    if cur >= goal:
        return True
    return False
print(canJump([2,3,1,1,4]))

# 45. Jump Game II
# Your goal is to reach the last index in the minimum number of jumps.
def minJump(nums):
    if not nums:
        return 0
    last_step_arrive, cur_step_arrive, step = 0, 0, 0
    for index,num in enumerate(nums):
        if index > last_step_arrive:
            step += 1
            last_step_arrive = cur_step_arrive
        cur_step_arrive = max(cur_step_arrive, index+num)
    if cur_step_arrive >= len(nums)-1:
        return step
    return -1
print(minJump([2,3,1,1,4]))

# 98. Validate Binary Search Tree
def valid_BST_inorder(root):
    if not root:
        return True
    def inorder(node, pre):
        if not node:
            return True
        if not inorder(node.left, pre):
            return False
        if node.val <= pre[0]:
            return False
        else:
            pre[0] = node.val
        if not inorder(node.right, pre):
            return False
        return True
    pre = [-float("inf")]
    return inorder(root, pre)
print(valid_BST_inorder(root))

def valid_BST(root):
    if not root:
        return True
    def util(node, left, right):
        if not node:
            return True
        if node.val <= left or node.val >= right:
            return False
        return util(node.left, left, node.val) and util(node.right, node.val, right)
    return util(root, -float("inf"), float("inf"))
print(valid_BST(root))


# 450. Delete Node in a BST
def deleteNode(root, key):
    if not root:
        return
    if root.val > key: # node on the left subtree
        root.left = deleteNode(root.left, key)
    elif root.val < key: # node on the right subtree
        root.right = deleteNode(root.right, key)
    else: # node is the root, so we need to delete the root
        if not root.left: # if the left subtree is empty, return right directly
            return root.right
        elif not root.right:
            return root.left
        else: # if node is root and it has left and right subtree, we can find a value that is min in right subtree or max in left
            temp = root.left
            maxi = temp.val
            while temp.right:
                temp = temp.right
                maxi = temp.val
            root.val = maxi
            root.left = deleteNode(root.left, root.val)
    return root




