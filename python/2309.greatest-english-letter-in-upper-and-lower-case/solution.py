# Created by asetti2002 at 2024/04/25 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def greatestLetter(self, s: str) -> str:
        import string
        uppercase = set(filter(lambda x: x.isupper(), s))
        lowercase = set(filter(lambda x: x.islower(), s))
        common_letters = uppercase.intersection(lowercase)
        if not common_letters:
            return ""
        return max(common_letters)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().greatestLetter(s)
    print("\noutput:", serialize(ans, "string"))
