import os # For implementing clear command and deletion of user file.
from diet import *


def clear():
    return os.system("clear")


def logo():
    clear()
    print(
        50 * x
        + "****************************************************************************\n"
        + 50 * x
        + "*           Applications of Linear Algebra in Linear Programming           *\n"
        + 50 * x
        + "*                         MAT 201 Linear Algebra                           *\n"
        + 50 * x
        + "****************************************************************************"
    )


def initialization():
    print("Press Spacebar to continue...")
    print("Press 0 to exit...")
    inp = input("Your Input:")
    if inp == " ":
        mainMenu()
    elif inp == "0":
        exit()
    else:
        initialization()


def mainMenu():
    clear()
    logo()
    print("1)Linear Equations in Multiple Variables")
    print("2)Non-Linear Equations in Multiple Variables")
    print("3)Project Details!")
    inp1 = input("Enter your choice:")
    if inp1 == "1":  # PAGE2(1)
        LinearProblems()
    elif inp1 == "2":
        pass
    elif inp1 == "3":  # PAGE2(3)
        projectdetails()
    else:
        print("Please enter a correct choice..!!!")



def projectdetails():
    clear()
    logo()
    details= open("ProjectDetails.txt", "r")
    print(details.read())

def LinearProblems():
    clear()
    logo()
    print("1) Diet Optimization")
    print("2) Profit Maximization")
    print("3) Supply-Chain Management")
    print("4) Custom Optimization")
    inp2 = input("Enter your choice:")
    if inp2 == "1":  
        DietOptimization()
    elif inp2 == "2":
        pass
    elif inp2 == "3":  # PAGE2(3)
        projectdetails()
    else:
        print("Please enter a correct choice..!!!")







#######################################
x= " "

logo()
initialization()


