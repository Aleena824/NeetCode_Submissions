#Method 1 - Sorting the characters to see if they give the same word/have the same number of characters
#Time complexity: O(n log n)  --> not that efficient
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t) #anagram should have same number of letters

#Method 2 - Using in-built counter function to count number of characters in each word
#Time complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)   