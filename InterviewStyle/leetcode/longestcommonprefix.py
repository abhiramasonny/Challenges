from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = strs[0]
        for i in strs:
            wsplit = list(i)
            #["f","l","o","w","r"]
            longestsplit = list(longest)
            nl = []
            for i in range(len(wsplit)-1):
                if wsplit[i] == longestsplit[i]:
                    nl.append(wsplit[i])
        return "".join(nl)
s = Solution()
print ( s.longestCommonPrefix(["flower", "flow", "flight"]))