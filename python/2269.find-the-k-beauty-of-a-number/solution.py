# Created by asetti2002 at 2024/04/25 20:28
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        def is_divisor(n, substring):
            if int(substring) == 0:
                return False
            return n % int(substring) == 0
        
        num_str = str(num)
        count = 0
        for i in range(len(num_str) - k + 1):
            substring = num_str[i:i + k]
            if is_divisor(num, substring):
                count += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().divisorSubstrings(num, k)
    print("\noutput:", serialize(ans, "integer"))
