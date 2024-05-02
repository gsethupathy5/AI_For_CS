# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/add-to-array-form-of-integer/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        carry = 0
        i = len(num) - 1
        
        while i >= 0 or k > 0 or carry > 0:
            n = num[i] if i >= 0 else 0
            total = n + k % 10 + carry
            res.append(total % 10)
            carry = total // 10
            i -= 1
            k //= 10
            
        return res[::-1]
# @lc code=end

if __name__ == "__main__":
    num: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().addToArrayForm(num, k)
    print("\noutput:", serialize(ans, "integer[]"))
