class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()

        s_cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
        if s_cleaned == s_cleaned[::-1]: #s[start : stop : step]
            return True
        else:
            return False