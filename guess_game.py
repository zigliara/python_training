# Guess game for testing Git branch
import random

def guess_number(guess_number):
    my_number = 0
    while my_number != guess_number:
        my_number = int(raw_input('Pick a number'))
        if my_number == guess_number:
            print 'You win Master!'
            break
        else:
            print 'Try again Test_branch_two'
            
def main():
    number = random.randint(1, 11)
    print number
    guess_number(number)
    
if __name__ == '__main__':
    main()
