### A character is palindrome in itself for e.g : "a" 
### If the next and the previous characters of "a" are same then the entire string along with those characters is a palindrome
### Here, there are 2 cases :
### (1) Input: s = "babad" Output: "bab" i.e Odd number Palindrome 
### (2) Input: s = "cbbd" Output: "bb" i.e Even number Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <=1 :
            return s

        def expand_centre(left,right) -> str:
            while left >= 0 and  right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
            return s[left+1 : right]
        
        max_str = s[0]
        for i in range(0,len(s)-1):
            odd = expand_centre(i,i)
            even = expand_centre(i,i+1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even
        
      return max_str
