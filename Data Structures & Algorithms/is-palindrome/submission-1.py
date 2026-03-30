class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers
        #i starts beginning
        #j starts at the end
        #skip over anything non alphanumerical
        #ignore spaces
        i = 0

        newS = ''
        for c in s:
            if c.isalnum():
                newS += c.lower()
        return newS == newS[::-1]