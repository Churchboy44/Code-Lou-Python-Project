'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
makes a temporary .txt file, uses regex to read from that file,
then uses the read values to calculate that game's winner and
displays them to the user, along withe the final scores
'''


p1 = input("Please enter player 1's name: ").split() #split turns p1 into list and ensures p1[0] is the whole input
p2 = input("Please enter the second player's name: ").split()

hole_num = 1
while True:
    answer = input('How many strokes did {} make on hole {}? Enter "done" to quit: '.format(p1[0], hole_num))
    if answer.lower() == 'done': #game-ending condition
        break
    else:
        p1.append((answer))

    p2.append(input('How many strokes did {} make on hole {}? '.format(p2[0], hole_num)))
    print()
    hole_num += 1

#creates temporary .txt file for later regex to read
with open ('golfGame.txt', "w") as scoreCard:
    for item in p1:
        scoreCard.write(item)
    scoreCard.write('\n')
    for item in p2:
        scoreCard.write(item)