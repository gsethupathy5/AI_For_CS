# Created by asetti2002 at 2024/04/25 19:33
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-gap/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def binaryGap(self, n: int) -> int:
        binary = bin(n)[2:]
        max_distance = 0
        distance = 0
        for i in range(len(binary)):
            if binary[i] == '1':
                if distance > 0:
                    max_distance = max(max_distance, distance)
                distance = 1
            elif distance > 0:
                distance += 1
        return max_distance
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().binaryGap(n)
    print("\noutput:", serialize(ans, "integer"))
