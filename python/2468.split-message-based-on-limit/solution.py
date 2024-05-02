# Created by asetti2002 at 2024/05/01 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/split-message-based-on-limit/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        result = []
        parts = (len(message) + limit - 1) // limit
        
        if parts > 26:
            return []
        
        for i in range(parts):
            suffix = "<{}/{}>".format(i+1, parts)
            start = i * limit
            end = min((i + 1) * limit, len(message))
            result.append(message[start:end] + suffix)
        
        return result
# @lc code=end

if __name__ == "__main__":
    message: str = deserialize("str", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().splitMessage(message, limit)
    print("\noutput:", serialize(ans, "string[]"))
