'tree, BFS, DFS, Recursion'
_author_ = "Jessie Wu"


class TreeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


class Solution(object):
    # 100. Same Tree
    # Given two binary trees, write a function to check if they are the same or not.
    # Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

    def same_tree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            flag1 = self.same_tree(p.left, q.left)
            flag2 = self.same_tree(p.right, q.right)
            if flag1 and flag2 and p.value == q.value:
                return True
            return False
# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(1)
# root2 = TreeNode(1)
# root2.left = TreeNode(2)
# root2.right = TreeNode(1)
# root2.left = TreeNode(1)
# so = Solution()
# print(so.same_tree(root1, root2))


# 101.Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
    def symmetric_tree(self, root):
        if not root:
            return True
        return self.symmetric_tree_util(root.left, root.right)

    def symmetric_tree_util(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.value != q.value:
            return False
        return self.symmetric_tree_util(p.left, q.right) and self.symmetric_tree_util(p.right, q.left)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(4)
# so = Solution()
# print(so.symmetric_tree(root))

# 104. Given a binary tree, find its maximum depth.
    def max_depth(self, root):
        if not root:
            return 0
        d1 = self.max_depth(root.left)
        d2 = self.max_depth(root.right)
        if d1 == 0:
            return d2+1
        elif d2 == 0:
            return d1+1
        else:
            return max(d1, d2)+1
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(4)
# so = Solution()
# print(so.max_depth(root))

# 111. Given a binary tree, find its minimum depth.
    def min_depth(self, root):
        if not root:
            return 0
        d1 = self.min_depth(root.left)
        d2 = self.min_depth(root.right)
        if d1 == 0:
            return d2+1
        elif d2 == 0:
            return d1+1
        else:
            return min(d1, d2)+1
#
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(4)
# so = Solution()
# print(so.min_depth(root))
# 110. Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
# subtrees of every node never differ by more than 1.
    def balanced_tree(self, root):
        if not root:
            return True
        return self.balanced_tree_util(root.left, root.right)

    def depth_tree(self, root):
        if not root:
            return 0
        d_left = self.depth_tree(root.left)
        d_right = self.depth_tree(root.right)
        if not root.left:
            return d_right+1
        elif not root.right:
            return d_left+1
        else:
            return max(d_right, d_left)+1

    def balanced_tree_util(self, p, q):
        if not p and not q:
            return True
        elif not p and q:
            if self.depth_tree(q) <= 1:
                return True
        elif not q and p:
            if self.depth_tree(p) <= 1:
                return True
        else:
            if abs(self.depth_tree(p) - self.depth_tree(q)) <= 1:
                return self.balanced_tree_util(p.left, p.right) and self.balanced_tree_util(q.left, q.right)
        return False
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(4)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(1)
# so = Solution()
# print(so.balanced_tree(root))

# 108. Convert Sorted Array to Binary Search Tree

    def convert_array_to_BST(self, array):
        if not array:
            return
        return self.convert_array_to_BST(0, len(array)-1, array)

    def convert_array_to_BST_util(self, left, right, array):
        if left > right:
            return
        while left <= right:
            middle = (right - left)//2
            root = TreeNode(array[middle])
            root.left = self.convert_array_to_BST_util(left, middle, array)
            root.right = self.convert_array_to_BST_unti(middle, right, array)
            return root

# 112. Path Sum
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
#  the path equals the given sum.

    def path_sum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.value == target
        return self.path_sum(root.left, target-root.value) or self.path_sum(root.right, target-root.value)
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(4)
# root.right.right = TreeNode(4)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(1)
# so = Solution()
# print(so.path_sum(root,10))

# 226. Invert Binary Tree
    def invert_tree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root


# 257. Binary Tree Paths
    def tree_path_stack(self, root):
        if not root:
            return []
        res = []
        stack = [(root, "")]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path + str(node.value))
            if node.right:
                stack.append((node.right, path + str(node.value) + "->"))
            if node.left:
                stack.append((node.left, path + str(node.value) + "->"))
        return res

    def tree_path_recursive(self, root):
        if not root:
            return []
        res = []
        self.tree_path_recursive_util(root, "", res)
        return res

    def tree_path_recursive_util(self, node, path, res):
        if not node.left and not node.right:
            res.append(path + str(node.value))
        if node.left:
            self.tree_path_recursive_util(node.left, path + str(node.value) + "->", res)
        if node.right:
            self.tree_path_recursive_util(node.right, path + str(node.value) + "->", res)



#  404. Sum of Left Leaves
    def sum_left_leaves(self, root):
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.value + self.sum_left_leaves(root.right)
        else:
            return self.sum_left_leaves(root.left) + self.sum_left_leaves(root.right)

    def sum_of_leaves(self, root):
        if not root:
            return 0
        res = 0
        if not root.left and not root.right:
            res += root.value
        else:
            res += (self.sum_of_leaves(root.left) + self.sum_of_leaves(root.right))
        return res


# 501. Find Mode in Binary Search Tree

    def mode_tree(self, root):
        dic = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.value not in dic:
                dic[node.value] = 1
            else:
                dic[node.value] += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        max_value = max(dic.values())
        return [k for k,v in dic.items() if v == max_value]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(4)
root.right.right.right = TreeNode(1)
so = Solution()
print(so.max_depth(root))
















