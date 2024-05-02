# Created by asetti2002 at 2024/05/01 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findScore(self, nums: List[int]) -> int:
        nums.sort()
        score = 0
        marked = [False] * len(nums)
        
        for i in range(len(nums)):
            if not marked[i]:
                score += nums[i]
                marked[i] = True
                if i-1 >= 0:
                    marked[i-1] = True
                if i+1 < len(nums):
                    marked[i+1] = True
        
        return score
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findScore(nums)
    print("\noutput:", serialize(ans, "long"))
