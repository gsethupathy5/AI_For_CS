# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/video-stitching/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    clips: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: int = deserialize("int", read_line())
    ans = Solution().videoStitching(clips, time)
    print("\noutput:", serialize(ans, "integer"))
