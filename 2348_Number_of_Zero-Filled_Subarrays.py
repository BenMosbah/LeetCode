class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        dict_trailing_zeros = {0: 0}
        for i in range(1, n + 1):
            if nums[i - 1] == 0:
                dict_trailing_zeros[i] = dict_trailing_zeros[i - 1] + 1
            else:
                dict_trailing_zeros[i] = 0

        def dp(n, nums):
            if n == 0:
                return 0
            else:
                return (dp(n - 1, nums) + dict_trailing_zeros[n])

        n = len(nums)
        return dp(n, nums)