# Turing Machine Index Suite
## About
The Turing Machine Index Suite is a command-line program written in Python with two operating modes for working with Turing machine indexing.
### Indexer Mode
Indexer mode accepts user-input instructions for a Turing machine as numbers separated by spaces, and calculates the index number for that machine according to the Prime Power Method.

```
Welcome to the Turing Machine Index Suite!
******************************************
Choose a mode:
a) Enter Turing machine instructions and receive an index number
b) Enter an index number and receive Turing machine instructions
c) Quit the program
Type a, b, or c and press enter: a

You chose indexer mode.
Enter a sequence of Turing machine instructions as non-negative integers delimited only by spaces.
The first instruction you enter should be 0, for the start state!
Enter instructions: 0 0 1 0 1 0 1 1 0 1

You entered the machine:
************************************
IN     READ    WRITE   GO TO   MOVE
0      0       1       0       1
0      1       1       0       1

The index for this machine is: 106743
```

### Decoder Mode
Decoder mode accepts a user-input index number and generates the instructions for its Turing machine according to the Prime Power Method, in a nicely-formatted chart.

```
Welcome to the Turing Machine Index Suite!
******************************************
Choose a mode:
a) Enter Turing machine instructions and receive an index number
b) Enter an index number and receive Turing machine instructions
c) Quit the program
Type a, b, or c and press enter: b

You chose decoder mode.
Enter a Turing machine index as a non-negative integer: 562790922834

INSTRUCTIONS FOR TURING MACHINE 562790922834
************************************
IN     READ    WRITE   GO TO   MOVE
0      1       1       0       1
0      0       1       1       1
1      0       1       2       0
```

## Usage
Run `main.py` in Python.
## License
This software is licensed under the GNU General Public License v3.0. See LICENSE for more details.
