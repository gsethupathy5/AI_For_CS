# Created by asetti2002 at 2024/05/01 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        def is_square_free(n):
            i = 2
            while i * i <= n:
                if n % (i * i) == 0:
                    return False
                i += 1
            return True
        
        def dfs(nums, pos, current_product, current_subset, res):
            if current_product != 1 and is_square_free(current_product):
                res[0] += 1
            for i in range(pos, len(nums)):
                dfs(nums, i + 1, current_product * nums[i], current_subset + [nums[i]], res)
        
        res = [0]
        dfs(nums, 0, 1, [], res)
        return res[0] % MOD
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().squareFreeSubsets(nums)
    print("\noutput:", serialize(ans, "integer"))
