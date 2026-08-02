class Solution:
    def findLatestTime(self, s: str) -> str:
        t = list(s)


        if t[0] == "?":
            if t[1] == "?" or t[1] <= "1":
                t[0] = "1"
            else:
                t[0] = "0"

       
        if t[1] == "?":
            if t[0] == "1":
                t[1] = "1"
            else:
                t[1] = "9"

       
        if t[3] == "?":
            t[3] = "5"

   
        if t[4] == "?":
            t[4] = "9"

        return "".join(t)
