# Created by asetti2002 at 2024/05/01 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/the-number-of-beautiful-subsets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        def backtrack(start, path):
            if abs(path) == k:
                return 
                
        count = 0
        backtrack(0, [])
        
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().beautifulSubsets(nums, k)
    print("\noutput:", serialize(ans, "integer"))
