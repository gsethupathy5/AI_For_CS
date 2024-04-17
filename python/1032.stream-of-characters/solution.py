# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/stream-of-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class StreamChecker:

    def __init__(self, words: List[str]):
        

    def query(self, letter: str) -> bool:
        

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    words: List[str] = deserialize("List[str]", constructor_params[0])
    obj = StreamChecker(words)

    for i in range(1, len(ops)):
        match ops[i]:
            case "query":
                method_params = split_array(params[i])
                letter: str = deserialize("str", method_params[0])
                ans = serialize(obj.query(letter))
                output.append(ans)

    print("\noutput:", join_array(output))
