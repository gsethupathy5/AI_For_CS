# Created by asetti2002 at 2024/04/25 20:27
# leetgo: 1.4.3
# https://leetcode.com/problems/fair-distribution-of-cookies/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort()
        i = 0
        j = len(cookies) - 1
        result = 0
        while i <= j:
            result = max(result, cookies[i] + cookies[j])
            i += 1
            j -= 1
        return result
# @lc code=end

if __name__ == "__main__":
    cookies: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().distributeCookies(cookies, k)
    print("\noutput:", serialize(ans, "integer"))
