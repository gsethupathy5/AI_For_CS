# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/distribute-candies-to-people/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        give_candies = 1
        
        while candies > 0:
            for i in range(num_people):
                if candies >= give_candies:
                    result[i] += give_candies
                    candies -= give_candies
                    give_candies += 1
                else:
                    result[i] += candies
                    candies = 0
                    break
        
        return result
# @lc code=end

if __name__ == "__main__":
    candies: int = deserialize("int", read_line())
    num_people: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(candies, num_people)
    print("\noutput:", serialize(ans, "integer[]"))
