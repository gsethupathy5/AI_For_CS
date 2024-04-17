# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    k: int = deserialize("int", read_line())
    fill: str = deserialize("str", read_line())
    ans = Solution().divideString(s, k, fill)
    print("\noutput:", serialize(ans, "string[]"))
