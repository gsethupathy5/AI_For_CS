# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    arrival: List[int] = deserialize("List[int]", read_line())
    load: List[int] = deserialize("List[int]", read_line())
    ans = Solution().busiestServers(k, arrival, load)
    print("\noutput:", serialize(ans, "integer[]"))
