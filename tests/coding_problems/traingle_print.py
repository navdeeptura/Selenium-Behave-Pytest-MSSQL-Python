
col = 6

def simple_training(c):
    for i in range(c):
        print("*"*i)

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i+1)

        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

a = pascal_triangle(6)

for i in a: print (i)