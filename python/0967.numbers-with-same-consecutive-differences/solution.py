# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        if n == 1:
            return [i for i in range(10)]
        
        def dfs(n, num, output):
            if n == 0:
                output.append(num)
                return
            tail_digit = num % 10
            next_digits = set([tail_digit + k, tail_digit - k])
            
            for next_digit in next_digits:
                if 0 <= next_digit < 10:
                    new_num = num * 10 + next_digit
                    dfs(n - 1, new_num, output)
        
        output = []
        for num in range(1, 10):
            dfs(n - 1, num, output)
        
        return output
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numsSameConsecDiff(n, k)
    print("\noutput:", serialize(ans, "integer[]"))
