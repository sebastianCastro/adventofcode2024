import re

word_soup = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

txt = word_soup.split()

grid = []
width = 0
for i in txt:
    row = []
    for j in i:
        row.append(j)
    grid.append(row)

for row in grid:
    print(row)