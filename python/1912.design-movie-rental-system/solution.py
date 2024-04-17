# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/design-movie-rental-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        

    def search(self, movie: int) -> List[int]:
        

    def rent(self, shop: int, movie: int) -> None:
        

    def drop(self, shop: int, movie: int) -> None:
        

    def report(self) -> List[List[int]]:
        

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    n: int = deserialize("int", constructor_params[0])
    entries: List[List[int]] = deserialize("List[List[int]]", constructor_params[1])
    obj = MovieRentingSystem(n, entries)

    for i in range(1, len(ops)):
        match ops[i]:
            case "search":
                method_params = split_array(params[i])
                movie: int = deserialize("int", method_params[0])
                ans = serialize(obj.search(movie))
                output.append(ans)
            case "rent":
                method_params = split_array(params[i])
                shop: int = deserialize("int", method_params[0])
                movie: int = deserialize("int", method_params[1])
                obj.rent(shop, movie)
                output.append("null")
            case "drop":
                method_params = split_array(params[i])
                shop: int = deserialize("int", method_params[0])
                movie: int = deserialize("int", method_params[1])
                obj.drop(shop, movie)
                output.append("null")
            case "report":
                ans = serialize(obj.report())
                output.append(ans)

    print("\noutput:", join_array(output))
