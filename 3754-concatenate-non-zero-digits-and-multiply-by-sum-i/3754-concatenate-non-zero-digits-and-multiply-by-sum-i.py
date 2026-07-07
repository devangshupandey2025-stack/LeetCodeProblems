class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        x = 0
        x_final = 0
        while(n > 0):
            k = n % 10
            if k != 0:
                s += k
                x = x*10 + k
            n = n // 10
        while(x > 0):
            k = x % 10
            x_final = x_final*10 + k
            x = x // 10
        return s * x_final