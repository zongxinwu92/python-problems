# backtracking problem
# three types problem, has template.

# 51. N-Queens
# typy3: return all possible ans
def isVaild(row, colForRow):
    for i in range(row):
        if colForRow[i] == colForRow[row] or abs(colForRow[row] - colForRow[i]) == row -i:
            return False
    return True

def helper(row, n, colForRow, path, res):
    if row == n:
        res.append(path)
        return
    else:
        for j in range(n):
            colForRow[row] = j
            if isVaild(row, colForRow):
                temp = "."*n
                helper(row+1, n, colForRow, path + [temp[:j]+"Q"+temp[j+1:n]], res)

def NQueens(n):
    res = []
    helper(0, n, [0]*n, [],res)
    return res
print(NQueens(4))

# 52. N-Queens II
# output valid number
def helperNQ(row, colForRow, n, count):
    if row == n:
        count[0] += 1
        return
    else:
        for index in range(n):
            colForRow[row] = index
            if isVaild(row, colForRow):
                helperNQ(row+1, colForRow, n, count)

def NQueenII(n):
    count = [0]
    helperNQ(0, [-1]*n, n, count)
    return count[0]
print(NQueenII(4))



#  77. Combinations
def help2(k, n, start, temp, res):
    if len(temp) == k:
        res.append(list(temp))
        return
    else:
        # for i in range(start, n+1):
            # temp.append(i)
            # help2(k, n, i+1, temp, res)
            # temp.pop()
        for i in range(start, n+1):
            help2(k, n, i+1, temp + [i], res)
def combination(k,n):
    res = []
    help2(k, n, 1, [], res)
    return res
print(combination(2,4))


# 39. Combination Sum
# Given a set of candidate numbers (C) (without duplicates) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
def help3(candidates, target, start, temp, res):
    if sum(temp) > target:
        return
    if sum(temp) == target:
        res.append(temp)
        return
    else:
        for index in range(start, len(candidates)):
            help3(candidates, target, index, temp + [candidates[index]], res)

def combinationSum(candidates, target):
    res = []
    candidates = sorted(candidates)
    help3(candidates, target, 0, [], res)
    return res
print(combinationSum([2, 3, 6, 7], 8))

# 40. Combination Sum II
# Given a collection of candidate numbers (C) and a target number (T),
# find all unique combinations in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.

def help5(candidates, target, start, temp, res):
    if sum(temp) > target:
        return
    if sum(temp) == target:
        res.add(tuple(temp))
        return
    else:
        for index in range(start, len(candidates)):
            help5(candidates, target, index+1, temp + [candidates[index]], res)

def combinationII(candidates, target):
    candidates = sorted(candidates)
    res = set() #since there is no duplicate in res
    help5(candidates, target, 0, [], res)
    return list(map(list, res))
print(combinationII([10, 1, 2, 7, 6, 1, 5], 8))

# 216. Combination Sum III
# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

def helper6(candidates, k, n, start, temp, res):
    if len(temp) > k or sum(temp) > n:
        return
    if len(temp) == k and sum(temp) ==n:
        res.append(temp)
        return
    else:
        for num in range(start, 10):
            helper6(candidates, k, n, num+1, temp + [num], res)
def combinationIII(k, n):
    candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []
    helper6(candidates, k, n, 1, [], res)
    return res
print(combinationIII(3, 7))

# 46. Permutations
def help4(nums, temp, res):
    if not nums:
        res.append(temp)
        return
    else:
        for index in range(len(nums)):
            help4(nums[index+1:len(nums)] + nums[:index], temp + [nums[index]], res)

def permutation(nums):
    res = []
    help4(nums, [], res)
    return res
print(permutation([1,2,3]))

# if duplicate in list:
