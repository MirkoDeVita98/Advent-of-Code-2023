with open("aoc4_input.txt") as infile:
    text = infile.read()

games = text.split('\n')


count = 0
for game in games:
  fil_game = game[game.find(':') + 1 :].split('|')
  num = fil_game[0].split(' ')
  win = fil_game[1].split(' ')

  pow = -1
  for el in win:
    if el != '' and el in num:
      pow += 1
  
  if pow != -1:
    count += (2**pow)

print(count)


bonus = [1 for i in range(len(games))]
for i, game in enumerate(games):
  fil_game = game[game.find(':') + 1:].split('|')
  num = fil_game[0].split(' ')
  win = fil_game[1].split(' ')

  j = 0
  for el in win:
    if el != '' and el in num:
      bonus[i + j + 1] += (bonus[i])
      j += 1
  

count = 0
for s in bonus:
  count += s

print(count)
