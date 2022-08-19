"""
1-Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.

2-Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced.

3-The clue can be multiples, divisible, greater or smaller, or a combination of all.
"""
import random
a=random.randrange(1,100)
numbers_of_gusses=1
print("Guess The Number Between the Range of 1 to 100 that Computer Choose For You. You Have Only 10 Chances.")
while(numbers_of_gusses<=10):
        n=int(input("Guess That Number: "))
        if int(n)<int(a):
          print("Your Number is Smaller Than the Computer's Choice")
        elif int(n)>int(a):
          print("Your Number is Greater Than the Computer's Choice")
        else:
            print("YOU WIN")
            print(numbers_of_gusses, "- No of Guesses you Take to Make the Correct Choice")
            print("Your score is {} Out of 100".format(100-numbers_of_gusses*10))
            break
        print(10 - numbers_of_gusses, "No of Guesses Left")
        numbers_of_gusses=numbers_of_gusses+1
if(numbers_of_gusses>=10):
    print("GAME OVER YOU LOSE")
