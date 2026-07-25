class Solution:
    def maxProduct(self, n: int) -> int:
        c = []
        while(n > 0):
            k = n % 10
            c.append(k)
            n = n // 10
        c_rev = sorted(c,reverse=True)
        return c_rev[0]*c_rev[1]