with open("aoc2_input.txt") as infile:
    games = infile.readlines()

tot = 0
for id, game in enumerate(games):

  words = game.split(' ')[2 : ]
  possible = True
  r = 12
  g = 13
  b = 14

  for i, word in enumerate(words):
    if word[0] == 'r':
      possible = possible and (int(words[i - 1]) <= r)
    elif word[0] == 'g':
      possible = possible and (int(words[i - 1]) <= g)
    elif word[0] == 'b':
      possible = possible and (int(words[i - 1]) <= b)

  if possible:
    tot += (id + 1)

print(tot)

tot = 0
for id, game in enumerate(games):

  words = game.split(' ')[2 : ]
  r = 0
  g = 0
  b = 0

  for i, word in enumerate(words):
    if word[0] == 'r':
      r = max(r, int(words[i - 1]))
    elif word[0] == 'g':
      g = max(g, int(words[i - 1]))
    elif word[0] == 'b':
      b = max(b, int(words[i - 1]))

  tot += (r*g*b)

print(tot)