# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        
        table_dict = defaultdict(lambda: defaultdict(int))
        food_items = set()
        
        for order in orders:
            table_number = order[1]
            food_item = order[2]
            food_items.add(food_item)
            table_dict[table_number][food_item] += 1
        
        food_items = sorted(food_items)
        result = [["Table"] + food_items]
        
        for table_number in sorted(table_dict, key=int):
            temp = [table_number]
            for food_item in food_items:
                temp.append(str(table_dict[table_number][food_item]))
            result.append(temp)
        
        return result
# @lc code=end

if __name__ == "__main__":
    orders: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().displayTable(orders)
    print("\noutput:", serialize(ans, "string[][]"))
