# Created by asetti2002 at 2024/05/01 20:17
# leetgo: 1.4.3
# https://leetcode.com/problems/count-increasing-quadruplets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] < nums[k] < nums[j] < nums[l]:
                            count += 1
                            
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().countQuadruplets(nums)
    print("\noutput:", serialize(ans, "long"))
