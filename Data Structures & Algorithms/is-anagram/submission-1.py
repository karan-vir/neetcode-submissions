class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)
        for char in s:
            s_freq[char]+= 1

        for char in t:
            t_freq[char]+= 1
        
        if t_freq == s_freq:
            return True
        else:
            return False

        # if sorted(s) == sorted(t):
        #     return True
        # else:
        #     return False
