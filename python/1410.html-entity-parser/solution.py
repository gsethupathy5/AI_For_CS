# Created by asetti2002 at 2024/04/25 20:40
# leetgo: 1.4.3
# https://leetcode.com/problems/html-entity-parser/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def entityParser(self, text: str) -> str:
        return text.replace("&quot;", "\"").replace("&apos;", "'").replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&frasl;", "/")
# @lc code=end

if __name__ == "__main__":
    text: str = deserialize("str", read_line())
    ans = Solution().entityParser(text)
    print("\noutput:", serialize(ans, "string"))
