class Solution(object):
    def rotate(self, matrix):
        # dimensions
        r = len(matrix)
        c = len(matrix[0])

        # create an empty r × c matrix
        result = [[0 for _ in range(c)] for _ in range(r)]

        # place each value in its rotated position
        for i in range(r):
            for j in range(c):
                # new row  = old column
                # new col  = (last row index) - old row
                result[j][r - 1 - i] = matrix[i][j]

        # copy the rotated picture back to the input matrix
        matrix[:] = result
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna