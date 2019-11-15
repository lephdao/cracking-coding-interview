# Complete the hourglassSum function below.
def hourglassSum(list):
    sum = 0
    for i in range(0, 4):
        for j in range(0, 4):
            thesum = list[i][j] + list[i][j + 1] + list[i][j + 2] + list[i + 1][j+1] + list[i + 2][j] + list[i + 2][j + 1] + list[i + 2][j + 2]
            if thesum > sum or i == 0 and j == 0:
                sum = thesum
    print(sum)

arr = [[1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
hourglassSum(arr)
arr2 = [[0, -4, -6, 0, -7, -6], [-1, -2, -6, -8, -3, -1], [-8, -4, -2, -8, -8, -6], [-3, -1, -2, -5, -7, -4], [-3, -5, -3, -6, -6, -6], [-3, -6, 0, -8, -6, -7]]
hourglassSum(arr2)
