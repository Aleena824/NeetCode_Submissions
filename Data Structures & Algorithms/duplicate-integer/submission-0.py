
#Method 1: Sorting approach

#Complexity:
'''Time: O(n log n) because of sorting
Space: O(1) extra space if the sort is in-place (Python’s sort may use extra internal space)'''
#Therefore, sorting method takes longer time

'''class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):#to prevent IndexError we take len-1
            if nums[i] == nums[i+1]:
                return True
        return False'''

#Method 2: Using set()
'''Here, even though we could use an empty list its not fast enough because a list iterates throug heach element inside it (linear search),
while a set uses has table lookup where each element has a unique key, so searching is faster in a set.'''

#Set has O(1) average time complexity for lookup while list has O(n) complexity for lookup

#COMPLEXITY
'''Time Complexity: O(n)You traverse the list at most once.Hash set lookups (i in checked_elements) and insertions (checked_elements.add(i)) take O(1) average time.
Space Complexity: O(n)In the worst-case scenario (where all elements are distinct), the checked_elements set will grow to store all n elements from the array.'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_elements = set()
        for i in nums:
            if i in checked_elements:
                return True
            checked_elements.add(i)
        return False
