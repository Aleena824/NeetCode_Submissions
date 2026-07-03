class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        
        num_counter = 1
        
        for check_num in range(1,len(nums)):
            if nums[check_num] != nums[check_num-1]:
                nums[num_counter] = nums[check_num]

                num_counter+=1

        return num_counter