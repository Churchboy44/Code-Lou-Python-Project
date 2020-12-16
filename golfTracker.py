'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
then returns the name of the winner and their score,
then asks if they want to play again
the info is then saved to a text file with a name chosen by the user'''


p1 = input("Please enter player 1's name: ").split() #split turns p1 into list and ensures p1[0] is the whole input
p2 = input("Please enter the second player's name: ").split()

hole_num = 1
while True:
    answer = input('How many strokes did {} make on hole {}? Enter "done" to quit: '.format(p1[0], hole_num))
    if answer.lower() == 'done': #game-ending condition
        break
    else:
        p1.append(int(answer))

    p2.append(int(input('How many strokes did {} make on hole {}? '.format(p2[0], hole_num))))
    print()
    hole_num += 1

#creates temporary .txt file for later regex to read
with open (file_name, "w") as scoreCard:
    for item in player1:
        scoreCard.write(item,' ')
    scoreCard.write('\n')
    for item in player2:
        scoreCard.write(item,' ')