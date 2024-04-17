# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/repeated-dna-sequences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().findRepeatedDnaSequences(s)
    print("\noutput:", serialize(ans, "string[]"))
