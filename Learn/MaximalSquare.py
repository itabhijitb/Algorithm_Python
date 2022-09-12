from functools import cache
from pprint import pprint
from typing import *


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp(i, j) = min(dp(i - 1, j), dp(i, j - 1), dp(i - 1, j - 1))
        # dp(i, j) = 0 if i, j < 0
        @cache
        def dp_td(i, j):
            nonlocal maxlen
            nonlocal dp_arr
            if i < 0 or j < 0:
                _len = 0
            elif matrix[i][j] == "1":
                _len = min(dp_td(i - 1, j), dp_td(i, j - 1),
                           dp_td(i - 1, j - 1)) + 1
                dp_arr[i][j] = _len
            else:
                dp_td(i - 1, j), dp_td(i, j - 1), dp_td(i - 1, j - 1)
                _len = 0
            maxlen = max(maxlen, _len)
            return _len

        def dp_bp():
            nonlocal maxlen
            dp_arr = [[0] * (max_col + 1) for _ in range(max_row + 1)]
            dp_arr[0][0] = int(matrix[0][0] == "1")
            for row in range(max_row):
                for col in range(max_col):
                    if matrix[row][col] == "1":
                        dp_arr[row][col] = min(dp_arr[row - 1][col - 1],
                                               dp_arr[row - 1][col],
                                               dp_arr[row][col - 1]) + 1
                        maxlen = max(maxlen, dp_arr[row][col])
            pprint(dp_arr)
        max_row = len(matrix)
        max_col = len(matrix[0])
        maxlen = 0

        dp_arr = [[0] * (max_col + 1) for _ in range(max_row + 1)]

        dp_td(max_row - 1, max_col - 1)
        pprint(dp_arr)
        print(maxlen)
        dp_bp()
        print(maxlen)
        return maxlen * maxlen


# Solution().maximalSquare([["0", "1", "1", "1", "0"], ["1", "1", "1", "1", "1"], [
#    "0", "1", "1", "1", "1"], ["0", "1", "1", "1", "1"], ["0", "0", "1", "1", "1"]])
Solution().maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
    "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
