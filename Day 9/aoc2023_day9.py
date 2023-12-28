with open("aoc9_input.txt") as infile:
    text = infile.read()

text = text.split('\n')

sequences = []

for row in text:
  nums = row.split(' ')
  sequences.append([int(x) for x in nums])


def history(sequence):

  values = [sequence[-1]]

  curr = sequence

  done = False
  while(not done):
    temp = []

    for i in range(len(curr) - 1):
      temp.append(curr[i + 1] - curr[i])
    
    values.append(temp[-1])

    curr = temp

    done = temp.count(0) == len(temp)
  
  prev = values[-1]

  for i, e in reversed(list(enumerate(values[: - 1]))):
    prev += e
  
  return prev

tot = 0

for sequence in sequences:
  tot += history(sequence)

print(tot)

tot = 0

for sequence in sequences:
  sequence.reverse()
  tot += history(sequence)

print(tot)