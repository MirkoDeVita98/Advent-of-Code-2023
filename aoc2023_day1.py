import re

with open('readme.txt') as infile:
    words = infile.readlines()


def calculate_cal(word):
  first = None
  last = None
  for c in word:
    if c >= '0' and c <= '9':
      if first == None:
        first = c
        last = c
      last = c
  return int(first + last)      

tot_cal = 0
for word in words:
  tot_cal += calculate_cal(word)

print(tot_cal)

def calibration(word):

  numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  i = len(word)
  first_num = ''
  j = -1
  second_num = ''
  for number in numbers:
    indexes = [
      match.start() for match in re.finditer(number, word)
    ]

    if len(indexes) > 0:
      if indexes[0] < i:
        i = indexes[0]
        first_num = number
      if indexes[-1] > j:
        j = indexes[-1]
        second_num = number

  ind_1 = numbers.index(first_num) % 10
  ind_2 = (numbers.index(second_num)) % 10

  num = str(ind_1) + str(ind_2)

  return int(num)

tot_cal = 0
for word in words:
  tot_cal += calibration(word)

print(tot_cal)