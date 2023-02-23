class Solution:
    def beautySum(self, s: str) -> int:
        def beauty(sub_s):
            max_ = 0
            min_ = 501
            for c in set(sub_s):
                count_c = sub_s.count(c)
                if count_c > max_:
                    max_ = sub_s.count(c)
                if count_c < min_:
                    min_ = sub_s.count(c)
            return max_ - min_

        def dp(s, n):
            if n < 3:
                return 0
            else:
                sum_of_beauties = 0
                for i in range(n - 2):
                    sub_s = s[i:n]
                    # print('Substring under scrutiny is : ',sub_s)
                    sum_of_beauties += beauty(sub_s)
                return dp(s, n - 1) + sum_of_beauties

        return dp(s, len(s))