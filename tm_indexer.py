##
# This program accepts numerical Turing machine instructions
# and calculates the index of that machine according to the Prime Power Method
##

import cmath    ## for square root function

## Determines whether a number is prime
def is_prime(number):
    ## Base cases:
    ## If the number is 2
    if number == 2:
        return True
    ## Else if number is less than 2
    elif number < 2:
        return False
    ## Else if number is even
    elif number % 2 == 0:
        return False

    ## For every other number starting with 3 until through the square root of number
    for i in range(3, int(cmath.sqrt(number).real)+1, 2):
        if number % i == 0:
            return False
    return True

## Takes a string of TM instructions and generates the proper index number
## Returns index of the Turing machine
def gen_index(instructions):
    ## if the instructions are empty
    if len(instructions) == 0:
        return 0    ## the index is 0
    index = 1   ## starts the index at 1
    current_prime = 1
    ## for every instruction in the list of instructions
    for i in range(len(instructions)):
        ## for the quantity of the current instruction
        for j in range(instructions[i]):
            index *= current_prime  ## multiplies the current index by the current prime
        ## Find and proceed to the next prime number
        next_prime_chosen = False ## True if current_prime has been changed to the next highest prime number
        while(next_prime_chosen == False):
            if current_prime < 3:
                current_prime += 1
            else:
                current_prime += 2
            next_prime_chosen = is_prime(current_prime)
    return index

## Print rows of instructions in a pretty format
def print_instructions(instruction_list):
    print("************************************")
    print("IN","READ","WRITE","GO TO","MOVE",sep='\t')
    for i in range(len(instruction_list)):
        print(instruction_list[i], "\t", sep='', end='')
        if i != 0 and i % 5 == 4:
            print()
    print()

## The main function
def main():
    ## Get Turing machine instructions from user input
    input_approved = False
    while input_approved == False:
        try:
            ## Get Turing machine instructions from user input
            tm_input = input("Enter a sequence of Turing machine instructions as non-negative integers delimited only by spaces.\nThe first instruction you enter should be 0, for the start state!\nEnter instructions: ")

            tm_instructions = tm_input.split() ## splits string of input into array of isolated instructions
            tm_instructions = list(map(int, tm_instructions)) ## converts str elements in list to int elements
            input_approved = True
        except (ValueError, TypeError):
            print("\nERROR: Invalid instructions not accepted. Try again!")
        except Exception as e:
            print("\nAn unexpected error occurred: ",e)
            print("Try again!")
    ## Shows the user what they entered in nicely-formatted presentation
    print()
    print("You entered the machine:")
    print_instructions(tm_instructions)
    ## Calculates the Turing machine index from the instructions
    print("The index for this machine is:",gen_index(tm_instructions)) ## calculate and print index number from instructions
