import re

with open("aoc5_input.txt") as infile:
    text = infile.read()

input = text.split('\n')

seeds = [int(s) for s in re.findall(r'\b\d+\b', input[0])]

seeds_2 = seeds.copy()

maps = ['seed-to-soil map:','soil-to-fertilizer map:','fertilizer-to-water map:','water-to-light map:','light-to-temperature map:','temperature-to-humidity map:','humidity-to-location map:']

last = ''
conv = [False for i in range(len(seeds))]
for i, line in enumerate(input[1 : ]):
  if line in maps:
    last = line
    conv = [False for i in range(len(seeds))]
    continue

  nums = [int(s) for s in re.findall(r'\b\d+\b', line)]
  
  if len(nums) == 3:
    for j, seed in enumerate(seeds):
      if seed >= nums[1] and seed <= nums[1] + nums[2] and not conv[j]:
          seeds[j] = nums[0] + (seed - nums[1])
          conv[j] = True

lowest = seeds[0]

for seed in seeds:
  lowest = min(lowest, seed)

print(lowest)

def process_intervals(a, b, c):
  conv = []
  not_conv = []
  if a[0] >= b[0] and a[0] <= b[0] + b[1]:
    new_start = c + (a[0] - b[0])
    new_range = min(a[0] + a[1], b[0] + b[1]) - a[0]
    conv.append((new_start, new_range))
    if new_range != a[1]:
      not_conv.append((a[0] + new_range, a[1] - new_range))
  elif b[0] >= a[0] and b[0] <= a[0] + a[1]:
    new_start = c
    new_range = min(a[0] + a[1], b[0] + b[1]) - b[0]
    conv.append((new_start, new_range))
    if a[0] < b[0]:
      not_conv.append((a[0], b[0] - a[0]))

    if a[0] + a[1] > b[0] + b[1]:
      not_conv.append((b[0] + b[1], a[0] + a[1] - b[0] - b[1]))
  else:
    not_conv.append(a)
    
  
  return conv, not_conv


to_process = []

for i in range(0, len(seeds_2), 2):
  to_process.append((seeds_2[i], seeds_2[i + 1]))

processed = []

for i, line in enumerate(input[1 : ]):
  if line in maps:
    temp = []
    for interval in to_process:
      if interval != (-1, -1):
        temp.append(interval)
    temp += processed
    to_process = temp.copy()
    processed = []
  else:
    nums = [int(s) for s in re.findall(r'\b\d+\b', line)]

    if len(nums) == 3:
      temp = []
      for j, seed in enumerate(to_process):
        if seed != (-1, -1):
          conv, not_conv = process_intervals(seed, (nums[1], nums[2]), nums[0])
          to_process[j] = (-1, -1)
          if conv:
            processed += conv
          if not_conv:
            temp += not_conv
      if temp:
        to_process += temp 

temp = []
for interval in to_process:
  if interval != (-1, -1):
    temp.append(interval)
temp += processed

lowest = temp[0][0]

for seed in temp:
  lowest = min(lowest, seed[0])

print(lowest)