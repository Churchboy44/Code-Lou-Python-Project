'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
then returns the name of the winner and their score,
then asks if they want to play again
the info is then saved to a text file with a name chosen by the user'''


p1 = input("Please enter player 1's name: ").split()
p2 = input("Please enter the second player's name: ").split()

count = 1
while True:
    answer = input('How many strokes did {} make on hole {}? Enter "done" to quit: '.format(p1[0], count)).lower()
    if answer == 'done':
        break
    else:
        p1.append(int(answer))

    p2.append(int(input('How many strokes did {} make on hole {}? '.format(p2[0], count))))
    print()
    count += 1