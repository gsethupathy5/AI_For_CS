# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

from typing import *
from leetgo_py import *

# @lc code=begin

class WordDictionary:

    def __init__(self):
        

    def addWord(self, word: str) -> None:
        

    def search(self, word: str) -> bool:
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = WordDictionary()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addWord":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                obj.addWord(word)
                output.append("null")
            case "search":
                method_params = split_array(params[i])
                word: str = deserialize("str", method_params[0])
                ans = serialize(obj.search(word))
                output.append(ans)

    print("\noutput:", join_array(output))
