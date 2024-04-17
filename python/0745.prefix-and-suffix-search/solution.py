# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/prefix-and-suffix-search/

from typing import *
from leetgo_py import *

# @lc code=begin

class WordFilter:

    def __init__(self, words: List[str]):
        

    def f(self, pref: str, suff: str) -> int:
        

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    words: List[str] = deserialize("List[str]", constructor_params[0])
    obj = WordFilter(words)

    for i in range(1, len(ops)):
        match ops[i]:
            case "f":
                method_params = split_array(params[i])
                pref: str = deserialize("str", method_params[0])
                suff: str = deserialize("str", method_params[1])
                ans = serialize(obj.f(pref, suff))
                output.append(ans)

    print("\noutput:", join_array(output))
