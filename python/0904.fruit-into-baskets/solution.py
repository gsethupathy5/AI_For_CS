# Created by asetti2002 at 2024/04/25 19:37
# leetgo: 1.4.3
# https://leetcode.com/problems/fruit-into-baskets/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        start = result = 0
        
        for end in range(len(fruits)):
            count[fruits[end]] = count.get(fruits[end], 0) + 1
            
            while len(count) > 2:
                count[fruits[start]] -= 1
                if count[fruits[start]] == 0:
                    del count[fruits[start]]
                start += 1
            
            result = max(result, end - start + 1)
        
        return result
# @lc code=end

if __name__ == "__main__":
    fruits: List[int] = deserialize("List[int]", read_line())
    ans = Solution().totalFruit(fruits)
    print("\noutput:", serialize(ans, "integer"))
