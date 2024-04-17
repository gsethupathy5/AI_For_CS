# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    requests: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maximumRequests(n, requests)
    print("\noutput:", serialize(ans, "integer"))
