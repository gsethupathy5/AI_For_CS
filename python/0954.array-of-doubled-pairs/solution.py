# Created by asetti2002 at 2024/04/25 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/array-of-doubled-pairs/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter
        
        arr.sort(key=abs)
        counter = Counter(arr)
        
        for num in arr:
            if counter[num] == 0:
                continue
            if counter[2 * num] == 0:
                return False
            counter[num] -= 1
            counter[2 * num] -= 1
        
        return True
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().canReorderDoubled(arr)
    print("\noutput:", serialize(ans, "boolean"))
