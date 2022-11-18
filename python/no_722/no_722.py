import re
from typing import List

# re 正则
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        return list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        m = len(source)
        in_comment = False
        res = []
        for i in range(m):
            if len(source[i]) == 0:
                continue
            j = 0
            comment_end = 0
            if not in_comment:
                cur_line = ""
            line_comment = False
            while j < len(source[i]):
                if j < len(source[i]) - 1 and source[i][j] == "/" and source[i][j + 1] == "/":
                    if in_comment:
                        j += 2
                        continue
                    line_comment = True
                    if j > comment_end:
                        cur_line += source[i][comment_end:j]
                    j = len(source[i])
                elif j < len(source[i]) - 1 and source[i][j] == "/" and source[i][j + 1] == "*":
                    if in_comment:
                        j += 1
                        continue
                    if j != 0:
                        cur_line += source[i][comment_end:j]
                    j += 2
                    in_comment = True
                elif j < len(source[i]) - 1 and source[i][j] == "*" and source[i][j + 1] == "/":
                    j += 1
                    if not in_comment:
                        continue
                    j += 1
                    comment_end = j
                    in_comment = False
                else:
                    j += 1
            if not line_comment and not in_comment:
                cur_line += source[i][comment_end: j]
            if not in_comment and cur_line:
                res.append(cur_line)

        return res