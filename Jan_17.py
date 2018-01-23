# 55. Jump Game
def canJump(nums):
    if not nums:
        return True
    goal = len(nums)-1
    cur = 0
    for index, num in enumerate(nums):
        if index <= cur:
            cur = max(cur, index + num)
    if cur >= goal:
        return True
    return False
print(canJump([3,2,1,0,4]))

 # 746. Min Cost Climbing Stairs
def climbStair(cost):
    if not cost:
        return 0
    opt_2, opt_1 = cost[0], cost[1]
    for index in range(2, len(cost)):
        opt_1, opt_2 = min(opt_1, opt_2) + cost[index], opt_1
    return min(opt_1, opt_2)
print(climbStair([10,15,20]))


# 724. Find Pivot Index
def pivot_index(nums):
    if not nums:
        return -1
    total = sum(nums)
    left_sum = 0
    for index, num in enumerate(nums):
        if left_sum == total - left_sum - nums[index]:
            return index
        else:
            left_sum += nums[index]
    return -1
print(pivot_index([1, 7, 3, 6, 5, 6]))

# 697. Degree of an Array
def degree_array(nums):
    if not nums:
        return 0
    left, right, count = {}, {}, {}
    for index, num in enumerate(nums):
        if num not in left:
            left[num] = index
        right[num] = index
        count[num] = count.get(num, 0)+1
    degree = max(count.values())
    ans = len(nums)
    for key in count:
        if count[key] == degree:
            ans = min(ans, right[key]-left[key]+1)
    return ans
print(degree_array([1, 2, 2, 3, 1]))

# 695. Max Area of Island
def max_area_island(grid):
    if not grid:
        return 0
    ans = 0
    visited = set()
    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            stack =[]
            if grid[i][j] == 1 and (i,j) not in visited:
                stack.append((i,j))
                visited.add((i,j))
                count = 1
                while stack:
                    node = stack.pop()
                    for offsetX, offsetY in ((-1,0),(1,0),(0,-1),(0,1)):
                        newX = offsetX + node[0]
                        newY = offsetY + node[1]
                        if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == 1:
                            if (newX, newY) not in visited:
                                stack.append((newX, newY))
                                visited.add((newX, newY))
                                count += 1
                ans = max(ans, count)
    return ans
print(max_area_island([[0,0,0,0,0,0,0,0]]))

# 200. Number of Islands
def num_island(grid):
    if not grid:
        return 0
    count = 0
    visited = set()
    row, col = len(grid), len(grid[0])
    for i in range(row):
        for j in range(col):
            stack = []
            if grid[i][j] == "1" and (i,j) not in visited:
                count += 1
                stack.append((i,j))
                visited.add((i,j))
                while stack:
                    node = stack.pop()
                    for offsetX, offsetY in ((-1,0), (1,0), (0,1),(0,-1)):
                        newX = offsetX + node[0]
                        newY = offsetY + node[1]
                        if 0 <= newX < row and 0 <= newY < col and grid[newX][newY] == "1":
                            if (newX, newY) not in visited:
                                stack.append((newX, newY))
                                visited.add((newX, newY))
    return count
print(num_island(["1","1","0","1","1"]))

# 463. Island Perimeter
def island_perimeter(grid):
    if not grid:
        return 0
    row, col = len(grid), len(grid[0])
    count = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                for offsetX, offsetY in ((-1,0),(1,0),(0,1),(0,-1)):
                    newX = offsetX + i
                    newY = offsetY + j
                    if newX >= row or newX < 0 or newY >= col or newY <0:
                        count += 1
                    elif grid[newX][newY] != 1:
                        count += 1
    return count

# 674. Longest Continuous Increasing Subsequence
def longest_increase_sub(nums):
    if not nums:
        return 0
    count = 1
    ans = 1
    for index in range(1, len(nums)):
        if nums[index] > nums[index-1]:
            count += 1
        else:
            ans = max(count, ans)
            count = 1
    return max(count, ans)

# 66. Plus One
def plus_one(nums):
    if not nums:
        return
    carry = 1
    for index in range(len(nums)-1, -1, -1):
        carry, nums[index] = divmod(nums[index]+carry, 10)
    if carry == 1:
        nums.insert(0, 1)
    return nums
print(plus_one([9,9,9]))

string = "12345"
for num in string:
    print(num)

# 392. Is Subsequence
def isSubsequence(s,t):
    if not s:
        return True
    if s and not t:
        return False
    index1, index2 = 0, 0
    while index1 < len(s) and index2 < len(t):
        if s[index1] == t[index2]:
            index1 += 1
            index2 += 1
        elif s[index1] != t[index2]:
            index2 += 1
    if index1 == len(s):
        return True
    return False
