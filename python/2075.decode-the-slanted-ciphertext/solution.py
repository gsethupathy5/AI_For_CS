# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/decode-the-slanted-ciphertext/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    encodedText: str = deserialize("str", read_line())
    rows: int = deserialize("int", read_line())
    ans = Solution().decodeCiphertext(encodedText, rows)
    print("\noutput:", serialize(ans, "string"))
