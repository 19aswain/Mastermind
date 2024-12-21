import random

ai = []
colours = ["red","blue","green","yellow"]
player = ""
pos1 = False
pos2 = False
pos3 = False
pos4 = False
guess1 = ""
guess2 = ""
guess3 = ""
guess4 = ""
win = False
attempts = 0

for i in range (4):
  ai.append(random.choice(colours))
print(ai)
while not win and attempts < 10:
  print("Type your guesses in: ")
  guess1 = input()
  guess1 = guess1.lower()
  guess2 = input()
  guess2 = guess2.lower()
  guess3 = input()
  guess3 = guess3.lower()
  guess4 = input()
  guess4 = guess4.lower()
  if guess1 == ai[0]:
    pos1 = True
    print("The first value is in the correct place")
  if guess2 == ai[1]:
    pos2= True
    print("The second value is in the correct place")
  if guess3 == ai[2]:
    pos3 = True
    print("The third value is in the correct place")
  if guess4 == ai[3]:
    pos4 = True
    print("The fourth value is in the correct place")
  if pos1 == True and pos2 == True and pos3 == True and pos4 == True:
    win = True
  if pos1 == False:
    if guess1 == ai[1] or guess1 == ai[2] or guess1 == ai[3]:
      print(f"The colour {guess1} is elsewhere in the sequence.")
  if pos2 == False:
    if guess2 == ai[0] or guess2 == ai[2] or guess2 == ai[3]:
      print(f"The colour {guess2} is elsewhere in the sequence.")
  if pos3 == False:
    if guess3 == ai[0] or guess3 == ai[1] or guess3 == ai[3]:
      print(f"The colour {guess3} is elsewhere in the sequence.")
  if pos4 == False:
    if guess4 == ai[0] or guess4 == ai[1] or guess4 == ai[2]:
      print(f"The colour {guess4} is elsewhere in the sequence.")
  attempts += 1
if not win == False:
    print("Well done, you win")
