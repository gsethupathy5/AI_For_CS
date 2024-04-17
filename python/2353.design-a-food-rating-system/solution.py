# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/design-a-food-rating-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        

    def changeRating(self, food: str, newRating: int) -> None:
        

    def highestRated(self, cuisine: str) -> str:
        

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    foods: List[str] = deserialize("List[str]", constructor_params[0])
    cuisines: List[str] = deserialize("List[str]", constructor_params[1])
    ratings: List[int] = deserialize("List[int]", constructor_params[2])
    obj = FoodRatings(foods, cuisines, ratings)

    for i in range(1, len(ops)):
        match ops[i]:
            case "changeRating":
                method_params = split_array(params[i])
                food: str = deserialize("str", method_params[0])
                newRating: int = deserialize("int", method_params[1])
                obj.changeRating(food, newRating)
                output.append("null")
            case "highestRated":
                method_params = split_array(params[i])
                cuisine: str = deserialize("str", method_params[0])
                ans = serialize(obj.highestRated(cuisine))
                output.append(ans)

    print("\noutput:", join_array(output))
