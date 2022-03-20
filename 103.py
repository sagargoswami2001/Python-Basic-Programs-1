# No. of Guesses he took to finish.
# n=27
# number_of_guesses=1
# print("Number of Guesses is Limited to Only 9 Times: ")
# while (number_of_guesses<=9):
#     guess_number = int(input("Guess the Number: "))
#     if guess_number<27:
#         print("You Enter Less Number Please Input Greater Number.\n")
#     elif guess_number>27:
#         print("You Enter Greater Number Please Input Smaller Number.\n ")
#     else:
#         print("You Won\n")
#         print(number_of_guesses,"No.of Guesses he took to Finish.")
#         break
#     print(9-number_of_guesses,"No. of Guesses Left")
#     number_of_guesses = number_of_guesses + 1

# if(number_of_guesses>9):
#     print("Game Over")


n = 18
num = 1
print("Number of Guesses is Limited to Only 9 Times: ")
while (num<=9):
    a = int(input("Guess the Number: "))
    if a<18:
        print("You Enter Less Number Please input Greater Number")
    elif a>18:
        print("You Enter Greater Number Please input Smaller Number")
    else:
        print("You Won")
        print(num,"No. of Guesses he took to Finish.")
        break
    print(9-num,"No. of Guesses Left")
    num = num + 1

if (num>9):
    print("Game Over")