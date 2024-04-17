# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/strong-password-checker/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    password: str = deserialize("str", read_line())
    ans = Solution().strongPasswordChecker(password)
    print("\noutput:", serialize(ans, "integer"))
