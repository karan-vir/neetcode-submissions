class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print
        if sorted(s) == sorted(t):
            return True
        else:
            return False