# Created by asetti2002 at 2024/04/25 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-squareful-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        import itertools
        
        def is_squareful(nums):
            for i in range(1, len(nums)):
                if int((nums[i-1] + nums[i]) ** 0.5) ** 2 != nums[i-1] + nums[i]:
                    return False
            return True
        
        count = 0
        for perm in set(itertools.permutations(nums)):
            if is_squareful(perm):
                count += 1
                
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numSquarefulPerms(nums)
    print("\noutput:", serialize(ans, "integer"))
