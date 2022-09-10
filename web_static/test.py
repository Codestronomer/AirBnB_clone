matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# n =
#      for no, row in enumerate(matrix) for i in range(0, len(row))]
# print(n)
n = []

for no, row in enumerate(matrix):
    if no == 0:
        n.extend(row)
    # elif no == len(row):
    #     n.extend(row[::-1])
    # else:
    #     n.extend(row[:len(row)-1])

print(n)
