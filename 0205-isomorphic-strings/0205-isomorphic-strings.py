class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1 = [-1] * 256
        hash2 = [-1] * 256

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            check_s = ord(s[i])
            check_t = ord(t[i])

            if hash1[check_s] == -1:
                hash1[check_s] = check_t

            if hash2[check_t] == -1:
                hash2[check_t] = check_s

            if hash1[check_s] != check_t or hash2[check_t] != check_s:
                return False

        return True