# Created by asetti2002 at 2024/05/01 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        dp = [0] * (10**6 + 1)
        
        for num in nums:
            for i in range(num, len(dp)):
                dp[i] = max(dp[i], dp[i - num] + 1)
        
        return [dp[q] for q in queries]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    queries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().answerQueries(nums, queries)
    print("\noutput:", serialize(ans, "integer[]"))
