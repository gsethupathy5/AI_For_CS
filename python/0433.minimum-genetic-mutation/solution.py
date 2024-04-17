# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-genetic-mutation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    startGene: str = deserialize("str", read_line())
    endGene: str = deserialize("str", read_line())
    bank: List[str] = deserialize("List[str]", read_line())
    ans = Solution().minMutation(startGene, endGene, bank)
    print("\noutput:", serialize(ans, "integer"))
