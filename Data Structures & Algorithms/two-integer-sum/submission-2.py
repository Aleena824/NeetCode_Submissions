class Solution:
    #Method 1: brute force, most inefficient as loop iterates every time
    #Time Complexity: O(n2)
    '''def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i!=j:
                    return [i,j]
    '''

    #Method 2: most efficient using has maps and enumerate(list_name) built in function in python
    #enumerate(list_name) is used to iterate in the form (index of element in the list, value of the element) in a loop
    #Time Complexity: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked_numbers ={} #an empty dictionary declared to store already checked elements of the nums list

        for index, num in enumerate(nums):
            '''for example, if target is 7 and we have a number 4, and we find the other number is 3, 
            then we return the indices of both values in the list called nums'''
            other_number = target - num #this is to check for the pair forming the sum of target

            if other_number in checked_numbers:
                return [checked_numbers[other_number], index] #return the indices of the found pair in a list that give the sum of target value

            checked_numbers[num]=index #otherwise, just add it to the dictionary if the pair is not found