with open("aoc7_input.txt") as infile:
    text = infile.read()

hands = text.split('\n')

class HandComparator(tuple):
    def __lt__(self, other):
        for i in range(len(self)):
            if self[i] != other[i]:
                return order_card[self[i]] < order_card[other[i]]
        return False

def inc_win(winning, rank, htype):
  for hand in sorted(htype, key=HandComparator):
    winning += dic[hand] * rank
    rank += 1

dic = {}
k5 = []
k4 = []
fh = []
k3 = []
tp = []
op = []
hc = []

order_card = {'A' : 12, 'K' : 11, 'Q' : 10, 'J' : 9, 'T' : 8, '9' : 7, '8' : 6, '7' : 5, '6' : 4, '5' : 3, '4' : 2, '3' : 1, '2' : 0}
for el in hands:
  count = [0] * len(order_card)
  hand, bid = el.split(' ')
  
  for c in hand:
    count[order_card[c]] += 1

  if max(count) == 5:
    k5.append(hand)
  elif max(count) == 4:
    k4.append(hand)
  elif max(count) == 3:
    if 2 in count:
      fh.append(hand)
    else:
      k3.append(hand)
  elif max(count) == 2:
    if count.count(2) == 2:
      tp.append(hand)
    else:
      op.append(hand)
  else:
    hc.append(hand)
  

  dic[hand] = int(bid)

winning = 0
rank = 1

winning, rank = inc_win(winning, rank, hc)
winning, rank = inc_win(winning, rank, op)
winning, rank = inc_win(winning, rank, tp)
winning, rank = inc_win(winning, rank, k3)
winning, rank = inc_win(winning, rank, fh)
winning, rank = inc_win(winning, rank, k4)
winning, rank = inc_win(winning, rank, k5)

print(winning)

#PART 2 WITH JOKERS

dic = {}
k5 = []
k4 = []
fh = []
k3 = []
tp = []
op = []
hc = []

order_card = {'A' : 12, 'K' : 11, 'Q' : 10, 'J' : 0, 'T' : 9, '9' : 8, '8' : 7, '7' : 6, '6' : 5, '5' : 4, '4' : 3, '3' : 2, '2' : 1}
for el in hands:
  count = [0] * len(order_card)
  hand, bid = el.split(' ')
  
  for c in hand:
    count[order_card[c]] += 1

  if count[0] > 0:
    for i in range(1, len(count)):
      if count[i] == max(count[1 :]):
        count[i] += count[0]
        count[0] = 0

  if max(count) == 5:
    k5.append(hand)
  elif max(count) == 4:
    k4.append(hand)
  elif max(count) == 3:
    if 2 in count:
      fh.append(hand)
    else:
      k3.append(hand)
  elif max(count) == 2:
    if count.count(2) == 2:
      tp.append(hand)
    else:
      op.append(hand)
  else:
    hc.append(hand)
  

  dic[hand] = int(bid)


winning = 0
rank = 1

winning, rank = inc_win(winning, rank, hc)
winning, rank = inc_win(winning, rank, op)
winning, rank = inc_win(winning, rank, tp)
winning, rank = inc_win(winning, rank, k3)
winning, rank = inc_win(winning, rank, fh)
winning, rank = inc_win(winning, rank, k4)
winning, rank = inc_win(winning, rank, k5)

print(winning)