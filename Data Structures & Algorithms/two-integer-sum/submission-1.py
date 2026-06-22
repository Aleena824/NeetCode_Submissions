class Solution:
    #Method 1: brute force, most inefficient as loop iterates every time
    #Complexity: O(n2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i,j]