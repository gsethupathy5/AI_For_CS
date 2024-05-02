# Created by asetti2002 at 2024/04/25 20:28
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        def can_get_candies(box):
            if opened[box]:
                return 0
            opened[box] = True
            res = candies[box]
            for key in keys[box]:
                has_keys[key] = True
            for cont_box in containedBoxes[box]:
                has_boxes[cont_box] = True
            return res
        
        n = len(status)
        opened = [False] * n
        has_keys = [False] * n
        has_boxes = [False] * n
        total_candies = 0
        
        while True:
            found_box = False
            for box in range(n):
                if has_boxes[box]:
                    found_box = True
                    total_candies += can_get_candies(box)
            if not found_box:
                break
            for box in range(n):
                if has_keys[box] and not opened[box]:
                    total_candies += can_get_candies(box)
        return total_candies
# @lc code=end

if __name__ == "__main__":
    status: List[int] = deserialize("List[int]", read_line())
    candies: List[int] = deserialize("List[int]", read_line())
    keys: List[List[int]] = deserialize("List[List[int]]", read_line())
    containedBoxes: List[List[int]] = deserialize("List[List[int]]", read_line())
    initialBoxes: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxCandies(status, candies, keys, containedBoxes, initialBoxes)
    print("\noutput:", serialize(ans, "integer"))
