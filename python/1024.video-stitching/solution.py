# Created by asetti2002 at 2024/04/25 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/video-stitching/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        dp = [float('inf')] * (time + 1)
        dp[0] = 0
        for start, end in clips:
            for i in range(start, min(end, time)+1):
                dp[i] = min(dp[i], dp[start] + 1)
            
        return -1 if dp[time] == float('inf') else dp[time]
# @lc code=end

if __name__ == "__main__":
    clips: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().videoStitching(clips, time)
    print("\noutput:", serialize(ans, "integer"))
