'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
makes a temporary .txt file, uses regex to read from that file,
then uses the read values to calculate that game's winner and
displays them to the user, along with the final scores
'''
import re
import io

temp_file_name = 'golfGame.txt'
def write_temp(p1, p2): # creates golfGame.txt for later regex to read
    with open(temp_file_name, "w") as f:
        for item in p1:
            f.write(item)
        f.write('\n')
        for item in p2:
            f.write(item)


def read_grab_names(): # returns player names from golfGame.txt
    with open(temp_file_name, "r") as f:
        content1 = f.readline()
        player1 = re.findall(r'^[A-z]+', content1)

        content2 = f.readline()
        player2 = re.findall(r'^[A-z]+', content2)
        # ^[A-z] keeps accidental words/mistypes from replacing player names
        # say golfGame.txt had Angus123donee on line 1 and Beef450 on line 2,
        # 'donee' won't be matched and Beef is still returned as player2[0]

        return player1[0], player2[0]


def read_grab_scores(): # returns list with strokes from each hole
    with open(temp_file_name, "r") as f:
        contents = f.read()
        golf_scores = re.findall(r'[1-9]+', contents)

        p1_score = 0
        for num in golf_scores[0]: # if findall = [('1','2','3'), ('4','5','6')]
            p1_score += int(num) # num is 1 2 3

        p2_score = 0
        for num in golf_scores[1]:
            p2_score += int(num) # num is 4 5 6

        return p1_score, p2_score


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
    print() #\n after the hole is done for readability
    hole_num += 1

write_temp(p1, p2)
p1_name, p2_name = read_grab_names()
p1_score, p2_score = read_grab_scores()

if p1_score < p2_score:
    print('And the winner is {} with {} strokes made!'.format(p1_name, p1_score))
elif p1_score == p2_score:
    print('Woah, its a tie! {} and {} both made {} strokes!'.format(p1_name, p2_name, p1_score))
else:
    print('And the winner is {} with {} strokes made!'.format(p2_name, p2_score))