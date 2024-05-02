# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i] ^ arr[i-1])
        return arr
# @lc code=end

if __name__ == "__main__":
    pref: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findArray(pref)
    print("\noutput:", serialize(ans, "integer[]"))
