class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        if numRows == 0:
            return ""
        cur_row = 0
        flag = False
        arr = [""] * numRows
        for i in s:
            arr[cur_row] += i
            if cur_row == 0 or cur_row == numRows-1:
                flag = not flag
            cur_row += 1 if flag else -1
        return(''.join(arr))