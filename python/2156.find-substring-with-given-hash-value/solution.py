# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/find-substring-with-given-hash-value/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    power: int = deserialize("int", read_line())
    modulo: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    hashValue: int = deserialize("int", read_line())
    ans = Solution().subStrHash(s, power, modulo, k, hashValue)
    print("\noutput:", serialize(ans, "string"))
