# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/stamping-the-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        pass
# @lc code=end

if __name__ == "__main__":
    stamp: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().movesToStamp(stamp, target)
    print("\noutput:", serialize(ans, "integer[]"))
