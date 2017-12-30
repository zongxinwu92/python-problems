'two sum and related problems'
_author_ = "Jessie Wu"

# number sum
# 1 two sum for force search
def twoSum_force(L,target):
    solution = []
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]+L[j] == target:
                solution.append([i,j])
    return solution
# print(twoSum_force([2,7,11,15],9)) # exactly one solution
# print(twoSum_force([2,2,7,11,15],9)) # have duplicate number in list
# print(twoSum_force([2,2,4,5,7,11,15],9)) # more than one solution

# use dict to search two sum
def twoSum_dict(nums, target):
    dic = {}
    solution = []
    for index, num in enumerate(nums):
        if num in dic:
            solution += [[a, index] for a in dic[num]]
        if target - num not in dic:
            dic[target - num] = [index]
        else:
            dic[target - num].append(index)
    return solution
# print(twoSum_dict([2,7,11,15],9)) # exactly one solution
# print(twoSum_dict([2,2,7,11,15],9)) # have duplicate number in list
# print(twoSum_dict([2,2,4,5,7,11,15],9)) # more than one solution

# 167 two sum for sorted array, no duplication and more than one solution
def twoSortedSum(nums, target):
    index1, index2 = 0, len(nums)-1
    solution = []
    while index1 < index2:
        if nums[index1] + nums[index2] == target:
            solution.append([index1, index2])
            index1 += 1
            index2 -= 1
        elif nums[index1] + nums[index2] > target:
            index2 -= 1
        else:
            index1 += 1
    return solution
print(two_sum_sorted_array([1,2,3,4,5],6))


# 15 3Sum (there is no duplication for the output)
def three_sum(nums, target):
    if len(nums) < 3:
        raise ValueError("error input")
    nums = sorted(nums)
    print(nums)
    solution = []
    for index in range(len(nums)):
        start, end = index + 1, len(nums) - 1
        while start < end:
            if nums[index] + nums[start] + nums[end] == target:
                solution.append((nums[index], nums[start], nums[end]))
                start += 1
                end -= 1
            elif nums[index] + nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1
    return list(set(solution))
print(three_sum([-1, 0, 1, 2, -1, -4], 0))

# 18 four sum
def four_sum(nums, target):
    pass
print(four_sum([1, 0, -1, 0, -2, 2], 0))

# 560 Subarray Sum Equals K
# Given an array of integers and an integer k, you need to find the total number of continuous
#  subarrays whose sum equals to k.

def subarray_sum_force(nums, k):
    if not nums:
        return 0
    count = 0
    for index in range(len(nums)):
        temp_sum = 0
        temp_index = index
        while temp_index < len(nums):
            temp_sum += nums[temp_index]
            if temp_sum == k:
                count += 1
            temp_index += 1
    return count
print(subarray_sum_force([1],0))

# in order to save time, we can record the sum, since sum[i,j] = sum[0,j] - sum[0, i-1], we can use a dict to record
# the number of time when same sum occur
def subarray_sum(nums, k):
    d = {}
    sum = 0
    count = 0
    for num in nums:
        sum = sum + num
        if sum == k: # occur directly, only one way (sum of all occur num)
            count += 1
        if sum - k in d:
            count += d[sum - k] # k = sum - (sum - k)
        if sum in d:
            d[sum] += 1
        else:
            d[sum] = 1
    return count
print(subarray_sum([0,-1,0,1,-1], 0))

# 653. Two Sum IV - Input is a BST
# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST
# such that their sum is equal to the given target.

class TreeNode(object):
    def __init__(self,x):
        self.value = x
        self.left = None
        self.right = None

    def two_sum_BST_method1(self, target, node): # use a set to store value of node, same as two sum
        pass
    



