class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST = {}
        mapTS = {}

        for i in range(len(s)):
            chS = s[i]
            chT = t[i]
            if chS in mapST:
                if mapST[chS] != chT:
                    return False
            else:
                mapST[chS] = chT

            if chT in mapTS:
                if mapTS[chT] != chS:
                    return False
            else:
                mapTS[chT] = chS

        return True
