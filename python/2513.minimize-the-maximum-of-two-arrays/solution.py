# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        low = max(divisor1 + 1, divisor2 + 1)
        high = 10**9
        
        while low < high:
            mid = (low + high) // 2
            arr1 = set([mid - i for i in range(uniqueCnt1)])
            arr2 = set([mid + i for i in range(uniqueCnt2)])
            
            if any(num % divisor1 == 0 for num in arr1) or any(num % divisor2 == 0 for num in arr2) or len(arr1.intersection(arr2)) > 0:
                low = mid + 1
            else:
                high = mid
        
        return low
# @lc code=end

if __name__ == "__main__":
    divisor1: int = deserialize("int", read_line())
    divisor2: int = deserialize("int", read_line())
    uniqueCnt1: int = deserialize("int", read_line())
    uniqueCnt2: int = deserialize("int", read_line())
    ans = Solution().minimizeSet(divisor1, divisor2, uniqueCnt1, uniqueCnt2)
    print("\noutput:", serialize(ans, "integer"))
