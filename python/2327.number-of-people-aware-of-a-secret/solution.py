# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    delay: int = deserialize("int", read_line())
    forget: int = deserialize("int", read_line())
    ans = Solution().peopleAwareOfSecret(n, delay, forget)
    print("\noutput:", serialize(ans, "integer"))
