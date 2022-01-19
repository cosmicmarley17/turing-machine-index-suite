##
# Main program to run the Turing machine indexer and decoder programs.
##

import tm_indexer
import tm_decoder

## Asks user which mode to run
## Returns 0 if indexer mode is chosen
## Returns 1 if decoder mode is chosen
## Exits the program if user chooses to quit
def choose_mode():
    while True:
        input_mode = input("Type a, b, or c and press enter: ")
        if input_mode == "a" or input_mode == "A":
            print("\nYou chose indexer mode.")
            return 0
        elif input_mode == "b" or input_mode == "B":
            print("\nYou chose decoder mode.")
            return 1
        elif input_mode == "c" or input_mode == "C":
            print("\nQuitting... goodbye!")
            exit()
        else:
            print("\nError: that wasn't an option.")

## Checks whether the user would like to run the program again.
## Returns True if the program is to be run again
def check_continue():
    while True:
        input_continue = input("Go again? (y/n): ")
        if input_continue == "y" or input_continue == "Y":
            return True
        elif input_continue == "n" or input_continue == "N":
            return False
        else:
            print("That wasn't an option.")

def main():
    print("Welcome to the Turing Machine Index Suite!")
    while True:
        print("******************************************")
        print("Choose a mode:")
        print("a) Enter Turing machine instructions and receive an index number")
        print("b) Enter an index number and receive Turing machine instructions")
        print("c) Quit the program")
        input_mode = choose_mode()  ## Prompts user to choose a mode
        if input_mode == 0:
            tm_indexer.main()   ## Runs the program to calculate index
        elif input_mode == 1:
            tm_decoder.main()   ## Runs the program to calculate instructions
        ## Asks the user if they want to go again
        if check_continue() == False:
            break
    print("Quitting... goodbye!")


################################################################################
## Runs main function
try:
    main()
## Politely quits program on CTRL+C
except KeyboardInterrupt:
    print("\nQuitting... goodbye!")
    exit()
