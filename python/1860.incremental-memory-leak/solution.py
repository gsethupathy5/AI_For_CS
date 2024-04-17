# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/incremental-memory-leak/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    memory1: int = deserialize("int", read_line())
    memory2: int = deserialize("int", read_line())
    ans = Solution().memLeak(memory1, memory2)
    print("\noutput:", serialize(ans, "integer[]"))
