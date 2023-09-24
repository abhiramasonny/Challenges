from typing import List
class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        if s[::-1] == s:
            return True
        for i in range(len(s)-1):
            if s[i] == "(":
                if s[i+1] != ")":
                    return False
            if s[i] == "{":
                if s[i+1] != "}":
                    return False
            if s[i] == "[":
                if s[i+1] != "]":
                    return False
        return True
            
                
s = Solution()
print (s.isValid("()[][}"))