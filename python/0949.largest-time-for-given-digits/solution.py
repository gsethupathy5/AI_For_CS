# Created by asetti2002 at 2024/04/25 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        import itertools
        max_time = -1
        for h, i, j, k in itertools.permutations(arr):
            hour = h * 10 + i
            minute = j * 10 + k
            if hour < 24 and minute < 60:
                max_time = max(max_time, hour * 60 + minute)
        
        if max_time == -1:
            return ""
        else:
            return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().largestTimeFromDigits(arr)
    print("\noutput:", serialize(ans, "string"))
