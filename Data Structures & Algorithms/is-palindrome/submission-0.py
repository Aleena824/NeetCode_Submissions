class Solution:
    def isPalindrome(self, s: str) -> bool:
        #new string in a different variable without special characters to check if palindrome
        newString = ""

        for i in s:
            if i.isalnum():
                newString+= i.lower()
        return newString == newString[::-1]