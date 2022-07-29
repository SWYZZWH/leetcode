# Design the basic function of Excel and implement the function of the sum formula.
#
# Implement the Excel class:
#
# Excel(int height, char width) Initializes the object with the height and the width of the sheet. The sheet is an integer matrix mat of size height x width with the row index in the range [1, height] and the column index in the range ['A', width]. All the values should be zero initially.
# void set(int row, char column, int val) Changes the value at mat[row][column] to be val.
# int get(int row, char column) Returns the value at mat[row][column].
# int sum(int row, char column, List<String> numbers) Sets the value at mat[row][column] to be the sum of cells represented by numbers and returns the value at mat[row][column]. This sum formula should exist until this cell is overlapped by another value or another sum formula. numbers[i] could be on the format:
# "ColRow" that represents a single cell.
# For example, "F7" represents the cell mat[7]['F'].
# "ColRow1:ColRow2" that represents a range of cells. The range will always be a rectangle where "ColRow1" represent the position of the top-left cell, and "ColRow2" represents the position of the bottom-right cell.
# For example, "B3:F7" represents the cells mat[i][j] for 3 <= i <= 7 and 'B' <= j <= 'F'.
# Note: You could assume that there will not be any circular sum reference.
#
# For example, mat[1]['A'] == sum(1, "B") and mat[1]['B'] == sum(1, "A").

# Constraints:
#
# 1 <= height <= 26
# 'A' <= width <= 'Z'
# 1 <= row <= height
# 'A' <= column <= width
# -100 <= val <= 100
# 1 <= numbers.length <= 5
# numbers[i] has the format "ColRow" or "ColRow1:ColRow2".
# At most 100 calls will be made to set, get, and sum.


from typing import List


# once a cell changes, all the numbers[i] includes this column should also change
# mat[i, j] -> [i, j, num]
class Excel:
    class RefInfo:
        def __init__(self, i: int, j: int, num: int):
            self.i = i
            self.j = j
            self.num = num

    class Cell:
        def __init__(self, i: int, j: int, val: int, excel: List[List["Cell"]]):
            self.i = i
            self.j = j
            self.val = val
            self.referred = {}
            self.refs = {}
            self.excel = excel

        def set_val(self, val: int):
            if val == self.val:
                return
            for i, rr in self.referred.items():
                for j, num in rr.items():
                    self.excel[i][j].update_val((val - self.val) * num)
            self.val = val

        def update_val(self, delta: int):
            self.set_val(self.val + delta)

        def ref(self, i: int, j: int):
            if i not in self.refs:
                self.refs[i] = {j: 1}
            elif j not in self.refs[i]:
                self.refs[i][j] = 1
            else:
                self.refs[i][j] += 1
            self.excel[i][j].be_referred(self.i, self.j)

        def be_referred(self, i: int, j: int):
            if i not in self.referred:
                self.referred[i] = {j: 1}
            elif j not in self.referred[i]:
                self.referred[i][j] = 1
            else:
                self.referred[i][j] += 1

        def no_more_referred(self, i: int, j: int):
            if i not in self.referred or j not in self.referred[i]:
                return
            self.referred[i].pop(j)

        def clear_refs(self):
            for i, rr in self.refs.items():
                for j, num in rr.items():
                    self.excel[i][j].no_more_referred(self.i, self.j)
            self.refs = {}

    def __init__(self, height: int, width: str):
        self.mat = [[]]
        w = ord(width) - ord('A') + 1
        self.mat = [[self.Cell(i, j, 0, self.mat) for j in range(w)] for i in range(height + 1)]
        for i in range(height + 1):
            for j in range(w):
                self.mat[i][j].excel = self.mat

    def set(self, row: int, column: str, val: int) -> None:
        column_idx = Excel.get_column_idx(column)
        self.sum(row, column, [])
        self.mat[row][column_idx].update_val(val - self.mat[row][column_idx].val)

    def get(self, row: int, column: str) -> int:
        column_idx = Excel.get_column_idx(column)
        return self.mat[row][column_idx].val

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        column_idx = Excel.get_column_idx(column)
        cell = self.mat[row][column_idx]
        cell.clear_refs()
        ret = 0
        for num_str in numbers:
            num_strs = num_str.split(":")
            if len(num_strs) == 1:
                c, r = Excel.get_column_idx(num_str[0]), int(num_str[1:])
                cell.ref(r, c)
                ret += self.mat[r][c].val
            else:
                c1, r1 = Excel.get_column_idx(num_strs[0][0]), int(num_strs[0][1:])
                c2, r2 = Excel.get_column_idx(num_strs[1][0]), int(num_strs[1][1:])
                for cc in range(c1, c2 + 1):
                    for rr in range(r1, r2 + 1):
                        ret += self.mat[rr][cc].val
                        cell.ref(rr, cc)
        cell.set_val(ret)
        return ret

    @staticmethod
    def get_column_idx(column: str) -> int:
        return ord(column) - ord('A')

# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
