class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = set(s)
        for let in letters:
            if s.count(let) == t.count(let):
                pass
            else:
                return False
        return True