# Created by asetti2002 at 2024/05/01 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximize-the-minimum-powered-city/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        pass
# @lc code=end

if __name__ == "__main__":
    stations: List[int] = deserialize("List[int]", read_line())
    r: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxPower(stations, r, k)
    print("\noutput:", serialize(ans, "long"))
