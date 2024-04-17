# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/most-popular-video-creator/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    creators: List[str] = deserialize("List[str]", read_line())
    ids: List[str] = deserialize("List[str]", read_line())
    views: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostPopularCreator(creators, ids, views)
    print("\noutput:", serialize(ans, "string[][]"))
