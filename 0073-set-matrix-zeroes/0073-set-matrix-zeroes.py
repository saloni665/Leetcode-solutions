class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c= len(matrix[0])
        row_tracker = [0 for _ in range(r)]
        col_tracker = [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix [i][j] == 0:
                    row_tracker[i] = -1
                    col_tracker[j] = -1

        for i in range(r):
            for j in range(c):
                if row_tracker[i] == -1 or col_tracker[j] == -1:
                    matrix [i][j] = 0            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna