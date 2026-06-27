class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict= {}
        if len(s) != len(t):
            return False

        count = {}
        for c in s:
            count[c] =  count.get(c, 0)+1
            
        for a in t:
            if a not in count:
                return False
            count[a] -= 1
            if count[a] <0:
                return False
        
        return True
    


        
        