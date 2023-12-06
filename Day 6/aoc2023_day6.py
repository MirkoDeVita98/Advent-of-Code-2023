import re

with open("aoc6_input.txt") as infile:
    text = infile.read()

input = text.split('\n')

times = [int(s) for s in re.findall(r'\b\d+\b', input[0])]
distances = [int(s) for s in re.findall(r'\b\d+\b', input[1])]


def bin_search(time, distance):
  i, j = 1, time

  found_1 = False
  result_1 = -1

  while not found_1:
    mid_1 = (i + j) // 2
    acc = time - mid_1

    if acc * mid_1 > distance and (acc + 1)*(mid_1 - 1) <= distance:
      found_1 = True
      result_1 = mid_1
    elif acc * mid_1 <= distance and (acc + 1)*(mid_1 - 1) <= distance:
      i = mid_1 + 1
    else:
      j = mid_1 - 1

  i, j = 0, time

  found_2 = False
  result_2 = -1

  while not found_2:
    mid_2 = (i + j) // 2
    acc = time - mid_2

    if acc * mid_2 <= distance and (acc + 1)*(mid_2 - 1) > distance:
      found_2 = True
      result_2 = mid_2 - 1
    elif acc * mid_2 > distance and (acc + 1)*(mid_2 - 1) > distance:
      i = mid_2 + 1
    else:
      j = mid_2 - 1



  return result_2 - result_1 + 1


ways = 1
for i in range(len(times)):
  ways *= bin_search(times[i], distances[i])

print(ways)


time_part_2 = [int(s) for s in re.findall(r'\b\d+\b', input[0].replace(" ", ""))][0]
distance_part_2 = [int(s) for s in re.findall(r'\b\d+\b', input[1].replace(" ", ""))][0]

print(bin_search(time_part_2, distance_part_2))