# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/stickers-to-spell-word/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    stickers: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().minStickers(stickers, target)
    print("\noutput:", serialize(ans, "integer"))
