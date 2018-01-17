class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(5)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
# 538. Convert BST to Greater Tree
def convert_BST(root):
    if not root:
        return
    sum_val = [0]
    convert_BST_util(root, sum_val)
    return root

def convert_BST_util(node, sum_val):
    if not node:
        return
    convert_BST_util(node.right, sum_val)
    node.val += sum_val[0]
    sum_val[0] = node.val
    convert_BST_util(node.left, sum_val)

# print(convert_BST(root))


# 102. Binary Tree Level Order Traversal
def traver_level(root):
    if not root:
        return
    res = []
    queue = [root]
    while queue:
        new_queue = []
        temp = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
            temp.append(node.val)
        res.append(temp)
        queue = new_queue
    return res
# print(traver_level(root))


# 103. Binary Tree Zigzag Level Order Traversal
def traverse_zigzag(root):
    if not root:
        return []
    res = []
    queue = [root]
    line = 1
    while queue:
        new_queue = []
        temp = []
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if  node.right:
                new_queue.append(node.right)
            temp.append(node.val)
        if line % 2 == 0:
            res.append(temp[::-1])
        else:
            res.append(temp)
        queue = new_queue
        line += 1
    return res
# print(traverse_zigzag(root))

# 572. Subtree of Another Tree
def isSame(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False
    else:
        if p.val == q.val:
            return isSame(p.left, q.left) and isSame(p.right, q.right)
        return False


def subtree(s, t):
    if not s and not t:
        return True
    elif not s or not t:
        return False
    else:
        if isSame(s, t):
            return True
    return subtree(s.left, t) or subtree(s.right, t)

# print(subtree(root2, root))


# 11. Container With Most Water
def max_container(height):
    if not height:
        return 0
    left, right = 0, len(height)-1
    container = 0
    while left < right:
        container = max(container, (right-left)*min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return container
height = [1,2, 1]
# print(max_container(height))

# 27. Remove Element
def remove_element(nums, val):
    if not nums:
        return 0
    if not val:
        return nums
    index = 0
    for num in nums:
        if num != val:
            nums[index] = num
            index += 1
    return index
nums = [2,2,2]
val = 2
# print(remove_element(nums, val))


# 26. Remove Duplicates from Sorted Array
def remove_duplicate(nums):
    if not nums:
        return 0
    res, index = 0, 1
    while index < len(nums):
        if nums[res] == nums[index]:
            index += 1
        else:
            res += 1
            nums[res] = nums[index]
    return res+1
# print(remove_duplicate([1,1,2]))


# 42. Trapping Rain Water
def trapping_rain(height):
    if not height:
        return 0
    l, r = 0, len(height)-1
    res = 0
    while l < r:
        lower = min(height[l], height[r])
        if height[l] == lower:
            l += 1
            while height[l] < lower:
                res += (lower - height[l])
                l += 1
        else:
            r -= 1
            while height[r] < lower:
                res += (lower- height[r])
                r -= 1
    return res
# print(trapping_rain([0,1,0,2,1,0,1,3,2,1,2,1]))


# 88. Merge Sorted Array (merge list2 into list1)

def merge_sorted(list1, m, list2, n):
    if not list2:
        return
    if not list1:
        list1 = [num for num in list2]
    while m > 0 and n > 0:
        if list2[n-1] > list1[m-1]:
            list1[m+n-1] = list2[n-1]
            n -= 1
        else:
            list1[m+n-1] = list1[m-1]
            m -= 1
    while n > 0:
        list1[n+m-1] = list2[n-1]
        n -= 1
    return list1



