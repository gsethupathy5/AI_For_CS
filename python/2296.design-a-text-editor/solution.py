# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/design-a-text-editor/

from typing import *
from leetgo_py import *

# @lc code=begin

class TextEditor:

    def __init__(self):
        

    def addText(self, text: str) -> None:
        

    def deleteText(self, k: int) -> int:
        

    def cursorLeft(self, k: int) -> str:
        

    def cursorRight(self, k: int) -> str:
        

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = TextEditor()

    for i in range(1, len(ops)):
        match ops[i]:
            case "addText":
                method_params = split_array(params[i])
                text: str = deserialize("str", method_params[0])
                obj.addText(text)
                output.append("null")
            case "deleteText":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                ans = serialize(obj.deleteText(k))
                output.append(ans)
            case "cursorLeft":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                ans = serialize(obj.cursorLeft(k))
                output.append(ans)
            case "cursorRight":
                method_params = split_array(params[i])
                k: int = deserialize("int", method_params[0])
                ans = serialize(obj.cursorRight(k))
                output.append(ans)

    print("\noutput:", join_array(output))
