def find_code(stop_row, stop_col):
    code = 20151125
    row = 1
    while True:
        for col in range(row):
            if (row - col) == stop_row and (col + 1) == stop_col:
                return code
            code = (code * 252533) % 33554393
        row += 1


print(find_code(2947, 3029))
