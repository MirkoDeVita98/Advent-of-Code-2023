with open("aoc8_input.txt") as infile:
    text = infile.read()

text = text.split('\n')
commands, nodes = text[0], text[2: ]

dic = {}

for node in nodes:
  temp = node.replace(" ", "").split('=')
  key = temp[0]
  temp2 = temp[1].replace("(", "").replace(")", "").split(',')
  pair = (temp2[0], temp2[1])
  dic[key] = pair

curr = 'AAA'
steps = 0
command = 0

while(curr != 'ZZZ'):
  steps += 1
  if commands[command] == 'L':
    curr = dic[curr][0]
  else:
    curr = dic[curr][1]

  command += 1
  if command == len(commands):
    command = 0

print(steps)

starts = []

for node in dic.keys():
  if node[-1] == 'A':
    starts.append(node)

steps = [0]*len(starts)

for i,start in enumerate(starts):
  curr = start
  step = 0
  command = 0

  while(curr[-1] != 'Z'):
    step += 1
    if commands[command] == 'L':
      curr = dic[curr][0]
    else:
      curr = dic[curr][1]

    command += 1
    if command == len(commands):
      command = 0
  
  steps[i] = step

from math import gcd
lcm = 1
for i in steps:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)