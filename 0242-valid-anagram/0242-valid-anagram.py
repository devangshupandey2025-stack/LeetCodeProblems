class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = [0]*26
        hash2 = [0]*26

        sub = 97

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            check_s = ord(s[i]) - sub
            check_t = ord(t[i]) - sub

            hash1[check_s] += 1
            hash2[check_t] += 1
            
        if hash1 == hash2:
            return True
        else:
            return False