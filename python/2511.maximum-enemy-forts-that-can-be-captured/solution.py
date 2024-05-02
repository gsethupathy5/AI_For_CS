# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        count = 0
        max_count = 0
        
        for i in range(len(forts)):
            if forts[i] == 1:
                count = 0
                for j in range(i+1, len(forts)):
                    if forts[j] == 0:
                        count += 1
                    elif forts[j] == -1:
                        break
                    max_count = max(max_count, count)
        
        return max_count
# @lc code=end

if __name__ == "__main__":
    forts: List[int] = deserialize("List[int]", read_line())
    ans = Solution().captureForts(forts)
    print("\noutput:", serialize(ans, "integer"))
