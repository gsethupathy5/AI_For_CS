# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    digits: str = deserialize("str", read_line())
    ans = Solution().letterCombinations(digits)
    print("\noutput:", serialize(ans, "string[]"))
