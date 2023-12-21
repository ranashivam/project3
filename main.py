# This is a sample Python script.
import random
import time


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBELMS = 5


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr =  str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    # print("Result of" + " ", expr, " is:", answer)
    return expr, answer

wrong = 0

print("Press Enter to Start")
print("--------------------")
startTime =  time.time()

for i in range(TOTAL_PROBELMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" +str(i +1) + ":  "  + expr + "= ")
        if guess == str(answer):
            break
        wrong = wrong + 1

endTime = time.time()
totalTime = round(endTime - startTime, 2)

print("--------------------")
print("Nice Work! You Took" , totalTime , "seconds to complete")

