'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
makes a temporary .txt file, uses regex to read from that file,
then uses the read values to calculate that game's winner and
displays them to the user, along with the final scores. I
recognize adding the file-reading is inefficient and it's here
purely for regex practice.
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
        player1 = re.findall(r'[-.A-z0-9 ]+ ', content1)

        content2 = f.readline()
        player2 = re.findall(r'[-.A-z0-9 ]+ ', content2)

        return player1[0], player2[0]


def read_grab_scores(): # returns list with strokes from each hole
    p1_name, p2_name = read_grab_names()
    p1_score = 0
    p2_score = 0

# ------ p1_score ------
    with open(temp_file_name, "r") as f:
        contents = f.read()
        golf_scores = re.findall(r' [0-9]+', contents)
        # starting at ' ' keeps weird names with numbers, like BB-8, from being read

        for i in range(1, len(golf_scores[0])): # if findall gives [(' ','1','2','3'), (' ','4','5','6')]
            p1_score += int(golf_scores[0][i]) # skip ' ', add 1 2 3

# ------ p2_score ------
    with open(temp_file_name, "r") as f:
        contents = f.read()
        golf_scores = re.findall(r' [0-9]+', contents)

        for i in range(1, len(golf_scores[1])): # if findall gives [(' ','1','2','3'), (' ','4','5','6')]
            p2_score += int(golf_scores[1][i]) # skip ' ', add 4 5 6

    return p1_score, p2_score


# ------ user input section ------
p1 = input("Please enter player 1's name: ").split() #split turns p1 into list and ensures p1[0] is the whole input
p2 = input("Please enter the second player's name: ").split()
p1.append(' ') # these spaces will tell read_grab_names where to stop reading
p2.append(' ')

hole_num = 1
answer = ''
while True:
    answer = input('How many strokes did {} make on hole {}? Enter "done" to quit: '.format(p1[0], hole_num))
    if answer.lower() == 'done': #game-ending condition
        break
    else:
        try: # if answer can't be changed to an int, this keeps it from being added to p1
            int(answer)
        except ValueError:
            print("Oops, that's not a number, please try again!")
            continue
        else:
            p1.append(answer)

    while True:
        try:
            answer = input('How many strokes did {} make on hole {}? '.format(p2[0], hole_num))
            int(answer)        
        except ValueError:
            print("Oops, that's not a number, please try again!")
        else:
            p2.append(answer)
            break

    print() #\n after the hole is done for readability
    hole_num += 1

write_temp(p1, p2)
p1_name, p2_name = read_grab_names()
p1_score, p2_score = read_grab_scores()

if p1_score < p2_score:
    print('And the winner is {}with {} strokes made!'.format(p1_name, p1_score))
elif p1_score == p2_score:
    print('Woah, its a tie! {}and {}both made {} strokes!'.format(p1_name, p2_name, p1_score))
else:
    print('And the winner is {}with {} strokes made!'.format(p2_name, p2_score))