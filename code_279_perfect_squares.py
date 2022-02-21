import math
class Solution:
    squares=[
        10000, 9801, 9604, 9409, 9216, 9025, 8836, 8649, 8464, 8281, 8100, 
        7921, 7744, 7569, 7396, 7225, 7056, 6889, 6724, 6561, 6400, 6241, 
        6084, 5929, 5776, 5625, 5476, 5329, 5184, 5041, 4900, 4761, 4624, 
        4489, 4356, 4225, 4096, 3969, 3844, 3721, 3600, 3481, 3364, 3249, 
        3136, 3025, 2916, 2809, 2704, 2601, 2500, 2401, 2304, 2209, 2116, 
        2025, 1936, 1849, 1764, 1681, 1600, 1521, 1444, 1369, 1296, 1225, 
        1156, 1089, 1024, 961, 900, 841, 784, 729, 676, 625, 576, 529, 
        484, 441, 400, 361, 324, 289, 256, 225, 196, 169, 144, 121, 
        100, 81, 64, 49, 36, 25, 16, 9, 4, 1
    ]

    def numSquares(self, n: int) -> int:
        if n in self.squares:
            return 1
        
        for i in range(int(pow(n,0.5))+1):
            if n-i*i == pow(int(pow(n-i*i,0.5)),2):
                return 2
        temp = n
        while temp % 4 == 0:
            temp = temp / 4
        if temp%8 == 7:
            return 4

        return 3

    def numSquares_dp(self, n:int) -> int:
        dp = [0] + [float('inf')]*n
        for i in range(1,n+1):
            j=1
            min_val = float('inf')
            while i-j*j >= 0:
                min_val = min(min_val, dp[i-j*j] +1)
                j += 1
            dp[i] = min_val
        return dp[-1]