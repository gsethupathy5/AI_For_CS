# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    recipes: List[str] = deserialize("List[str]", read_line())
    ingredients: List[List[str]] = deserialize("List[List[str]]", read_line())
    supplies: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findAllRecipes(recipes, ingredients, supplies)
    print("\noutput:", serialize(ans, "string[]"))
