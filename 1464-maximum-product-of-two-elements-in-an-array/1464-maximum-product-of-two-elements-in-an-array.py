class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n_rev = sorted(nums, reverse=True)
        return (n_rev[0] - 1) * (n_rev[1] - 1)