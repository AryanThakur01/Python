'''
1. Two Sum
EASY

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''





'''Time Limit Exceeded'''
# class Solution:
#     def findNum2Index(self, num1Index, nums, target):
#         sum = nums[num1Index]
#         left = 0
#         while sum !=target :
#             mid = int((num1Index + left) /2)
#             if nums[mid] + nums[num1Index] == target:
#                 return [mid, num1Index]
#             elif nums[mid]*2 >target:
#                 num1Index = mid
#             elif nums[mid]*2 <target:
#                 left = mid
#             else:
#                 if mid == 0:
#                     return [0,1]
#                 elif nums[mid-1] == nums[mid]:
#                     return [mid-1, mid]
#                 else:
#                     return [mid, mid+1]


#     def twoSum(self, nums, target):
#         num1Index = 0
#         sum = 0
#         for i in range(0, len(nums)):
#             if(nums[i]> target):
#                 num1Index=i-1
#                 break
#             else:
#                 num1Index = i
#         return self.findNum2Index(num1Index, nums, target)


'''This solution is valid only if the given list is sorted'''

# class Solution:
#     def twoSum(self, nums, target):
#         nums.sort()
#         left = 0
#         right = len(nums)-1
#         while nums[left] + nums[right] != target:
#             mid = int((left + right)/2)
#             if nums[mid]*2 == target:
#                 if nums[mid] == nums[mid+1]:
#                     return [mid, mid+1]
#                 else:
#                     return [mid-1, mid]

#             elif nums[mid]*2 < target:
#                 left = mid

#             else:
#                 right = mid

#         return [left, right]



class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]




'''Best Solution'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        if not nums: return []
        for i, num in enumerate(nums):
            comp = target - num
            if comp in dic:
                return [i, dic[comp]]
            else:
                dic[num] = i