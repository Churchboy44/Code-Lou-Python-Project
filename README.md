# Code-Lou-Python-Project

Author: Stephen Lorenz

---Info---

golfTracker.py is a simple program that asks the user for the names of 2 golf players
then asks for the number of strokes they made on each hole, storing the name and
values in lists p1 and p2. The name of the players are stored at p1[0] and p2[0]
respectively. On p1's turn, the user is given the option to quit by inputing the word
"done". ValueErrors during the loop are handled with an error message and the loop
continues. When a game ends, the contents of p1 and p2 are written to a temporary
.txt file. The .txt is then read by regex code and the numbers are converted to ints
and are used to calculate the final scores. The user is shown the winner's and
loser's names (read from the .txt) and their respective scores. I know this isn't
the most efficient way to do this, but I needed regex practice and a 3rd requirement
to meet.

---Chosen Requirements---

* Implement a “master loop” console application where the user can repeatedly enter
commands/perform actions, including choosing to exit the program
* Read data from an external file, such as text, JSON, CSV, etc and use that data in your
application
* Create a dictionary or list, populate it with several values, retrieve at least one value, and
use it in your program
* Create and call at least 3 functions, at least one of which must return a value that is used
