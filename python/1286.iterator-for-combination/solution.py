# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/iterator-for-combination/

from typing import *
from leetgo_py import *

# @lc code=begin

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        

    def next(self) -> str:
        

    def hasNext(self) -> bool:
        

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    characters: str = deserialize("str", constructor_params[0])
    combinationLength: int = deserialize("int", constructor_params[1])
    obj = CombinationIterator(characters, combinationLength)

    for i in range(1, len(ops)):
        match ops[i]:
            case "next":
                ans = serialize(obj.next())
                output.append(ans)
            case "hasNext":
                ans = serialize(obj.hasNext())
                output.append(ans)

    print("\noutput:", join_array(output))
