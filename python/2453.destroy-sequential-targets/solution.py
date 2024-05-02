# Created by asetti2002 at 2024/05/01 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/destroy-sequential-targets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        max_targets = 0
        
        for num in nums:
            count = 1
            while num + count * space in nums:
                count += 1
            if count > max_targets:
                max_targets = count
                result = num
        
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    space: int = deserialize("int", read_line())
    ans = Solution().destroyTargets(nums, space)
    print("\noutput:", serialize(ans, "integer"))
