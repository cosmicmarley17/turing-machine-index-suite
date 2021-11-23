##
# This program accepts a Turing machine index and calculates
# the instructions of that machine according to the Prime Power Method
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

    ## For every other real num starting with 3 until through the square root of 'number'
    for i in range(3, int(cmath.sqrt(number).real)+1, 2):
        if number % i == 0:
            return False
    return True

## Returns the prime factorization of a given product in a list in which each
## element at position n corresponds to the nth prime number and the element's value
## is the multiple of the nth prime number in the prime factorization
## of the input product
def prime_factorize(product):
    instructions = [0,0]
    pos = 1
    prime_divisor = 2
    while product > 1:
        if is_prime(prime_divisor):
            while product % prime_divisor == 0:
                product = product//prime_divisor    ## the '//' does integer division with higher precision with large numbers
                instructions[pos] += 1 ## increment value of current instruction
            pos += 1 ## move to next instruction
            instructions.append(0) ## increase size of instructions list
        if prime_divisor == 2:
            prime_divisor = 3
        else:
            prime_divisor += 2

    while len(instructions) % 5 != 0:
        ## if there's a trailing 0 on a row by itself
        if len(instructions) % 5 == 1:
            instructions.pop() ## remove unintended trailing 0
            break
        ## if the product is 0 (empty instruction)
        if product == 0:
            instructions = []
        else:
            instructions.append(0) ## increase size of list
    return instructions

## Print rows of instructions in a pretty format
def print_instructions(instruction_list, tm_index):
    print()
    print("INSTRUCTIONS FOR TURING MACHINE",tm_index)
    print("************************************")
    print("IN","READ","WRITE","GO TO","MOVE",sep='\t')
    for i in range(len(instruction_list)):
        print(instruction_list[i], "\t", sep='', end='')
        if i != 0 and i % 5 == 4:
            print()
    print()

## The main function
def main():
    ## Get Turing machine index from user input
    input_approved = False
    while input_approved == False:
        try:
            tm_index = int(input("Enter a Turing machine index as a non-negative integer: "))
        except KeyboardInterrupt:
            print("\nQuitting... goodbye!")
            exit()
        except:
            print("Invalid input! Must be a non-negative integer")
            continue
        ## Accept integer only if it's non-negative
        if tm_index >= 0:
            input_approved = True
        else:
            print("Invalid input! Must be a non-negative integer")
    ## Decode number to lines of instructions and print them
    print_instructions(prime_factorize(tm_index),tm_index)
