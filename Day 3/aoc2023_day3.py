from collections import defaultdict

with open("aoc3_input.txt") as infile:
    text = infile.read()

grid = text.split('\n')

def isspecial(c):
  return c != '.' and not c.isdecimal()

count = 0
for i, row in enumerate(grid):
  start = -1
  valid = False
  for j, digit in enumerate(row):
    if digit.isdecimal():
      if start == -1:
        start = j
      
      if not valid:
        if j < len(row) - 1:
          valid = valid or isspecial(grid[i][j + 1]) 
        if j > 0:
          valid = valid or isspecial(grid[i][j - 1])
        if i < len(grid) - 1 and j < len(row) - 1:
          valid = valid or isspecial(grid[i + 1][j + 1])
        if i < len(grid) - 1:
          valid = valid or isspecial(grid[i + 1][j])
        if i < len(grid) - 1 and j > 0:
          valid = valid or isspecial(grid[i + 1][j - 1])
        if i > 0 and j < len(row) - 1:
          valid = valid or isspecial(grid[i - 1][j + 1])
        if i > 0:
          valid = valid or isspecial(grid[i - 1][j])
        if i > 0 and j > 0:
          valid = valid or isspecial(grid[i - 1][j - 1])
    else:
      if start != -1 and valid:
        count += int(row[start : j])
      valid = False
      start = -1
  if start != -1 and valid:
      count += int(row[start : ])

print(count)

def isspecial(c):
  return c == '*'

dic = defaultdict(lambda : [])
for i, row in enumerate(grid):
  start = -1
  valid = False
  pos = -1
  for j, digit in enumerate(row):
    if digit.isdecimal():
      if start == -1:
        start = j
      
      if not valid:
        if j < len(row) - 1:
          if isspecial(grid[i][j + 1]):
            pos = (i, j + 1)
            valid = True
        if j > 0:
          if isspecial(grid[i][j - 1]):
            pos = (i, j - 1)
            valid = True
        if i < len(grid) - 1 and j < len(row) - 1:
          if isspecial(grid[i + 1][j + 1]):
            pos = (i + 1, j + 1)
            valid = True
        if i < len(grid) - 1:
          if isspecial(grid[i + 1][j]):
            pos = (i + 1, j)
            valid = True
        if i < len(grid) - 1 and j > 0:
          if isspecial(grid[i + 1][j - 1]):
            pos = (i + 1, j - 1)
            valid = True
        if i > 0 and j < len(row) - 1:
          if isspecial(grid[i - 1][j + 1]):
            pos = (i - 1, j + 1)
            valid = True
        if i > 0:
          if isspecial(grid[i - 1][j]):
            pos = (i - 1, j)
            valid = True
        if i > 0 and j > 0:
          if isspecial(grid[i - 1][j - 1]):
            pos = (i - 1, j - 1)
            valid = True
    else:
      if start != -1 and valid:
        dic[pos].append(int(row[start : j]))
      valid = False
      start = -1
      pos = -1
  if start != -1 and valid:
        dic[pos].append(int(row[start : ]))

count = 0
for nums in dic.values():
  if len(nums) == 2:
    count += nums[0] * nums[1]

print(count)