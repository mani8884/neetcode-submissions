class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict= {}

        def counter(t):
            f = {}
            for c in t:
                f[c] =  f.get(c, 0)+1
            return f
        
        s_dict = counter(s)
        t_dict= counter(t)
        if s_dict==t_dict:
            return True
        return False
    


        
        