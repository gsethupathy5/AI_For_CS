# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/implement-magic-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin

class MagicDictionary:

    def __init__(self):
        

    def buildDict(self, dictionary: List[str]) -> None:
        

    def search(self, searchWord: str) -> bool:
        

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = MagicDictionary()

    for i in range(1, len(ops)):
        match ops[i]:
            case "buildDict":
                method_params = split_array(params[i])
                dictionary: List[str] = deserialize("List[str]", method_params[0])
                obj.buildDict(dictionary)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                searchWord: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(searchWord))
                output.append(ans)

    print("\noutput:", join_array(output))
