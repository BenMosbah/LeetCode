class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        biggest_to_the_left = [-1e5]*n
        smallest_to_the_right = [1e5]*n
        for i in range(1, n-1):
            biggest_to_the_left[i] = max(nums[i-1], biggest_to_the_left[i-1])
        for i in range(n-1, 1, -1):
            smallest_to_the_right[i-1] = min(nums[i], smallest_to_the_right[i])

        total_beauty = 0

        for i in range(1,n-1):
            if biggest_to_the_left[i] < nums[i] < smallest_to_the_right[i]:
                total_beauty += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total_beauty +=1

        return total_beauty