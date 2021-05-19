from typing import Mapping
import numpy as np
import os
import time

from numpy.core.records import array
import simplex
from simplex import *
# import csv

global proteinConst, carbsConst, fatConst, calorieConst
nutriComp=[]
x=' '

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

def Reader(x):
    with open("FoodChart.txt", "r") as chart:

    
        chartFile = chart.read().splitlines()
        iRow= chartFile[x].split()
        components= iRow[1:5]
        nutriComp.append(components)
        temp= np.array(nutriComp)
        global floatNutriComp
        floatNutriComp = temp.astype(np.float)
        return floatNutriComp

def constSequencing():
        global proteinConst,carbsConst,fatConst,calorieConst
        proteinConst= []
        carbsConst= []
        fatConst=[]
        calorieConst=[]
        for i in np.nditer(floatNutriComp[:, 0:1]):
                a=float(i)
                proteinConst.append(a)
        print("Protein Array = " ,proteinConst)

        for i in np.nditer(floatNutriComp[:, 1:2]):
                a=float(i)
                carbsConst.append(a)
        print("Carbohydrate Array = " ,carbsConst)

        for i in np.nditer(floatNutriComp[:, 2:3]):
                a=float(i)
                fatConst.append(a)
        print("Fat Array = " ,fatConst)

        for i in np.nditer(floatNutriComp[:, 3:4]):
                a=float(i)
                calorieConst.append(a)
        print("Calorie Array = " ,calorieConst)
        return proteinConst, carbsConst, fatConst, calorieConst
                


def FoodChoices():
        clear()
        logo()

        foodChart= open("FoodNames.txt", 'r')
        content = foodChart.read()
        print(content)
        userInput= (input("Enter the serial numbers of your Food Choices from the given chart: "))
        userList= userInput.split(' ')
        for i in userList:
                if(int(i)>20 or int(i)<0):
                        print("Invalid Choices Found! Please try again :)")
                        time.sleep(3)
                        FoodChoices()
        flag=0
        for x in userList:
                if(x=='1'):
                        Reader(0)
                elif(x=='2'):
                        Reader(1)
                elif(x=='3'):
                        Reader(2)
                elif(x=='4'):
                        Reader(3)
                elif(x=='5'):
                        Reader(4)
                elif(x=='6'):
                        Reader(5)
                elif(x=='7'):
                        Reader(6)
                elif(x=='8'):
                        Reader(7)
                elif(x=='9'):
                        Reader(8)
                elif(x=='10'):
                        Reader(9)
                elif(x=='11'):
                        Reader(10)
                elif(x=='12'):
                        Reader(11)
                elif(x=='13'):
                        Reader(12)
                elif(x=='14'):
                        Reader(13)
                elif(x=='15'):
                        Reader(14)
                elif(x=='16'):
                        Reader(15)
                elif(x=='17'):
                        Reader(16)
                elif(x=='18'):
                        Reader(17)
                elif(x=='19'):
                        Reader(18)
                elif(x=='20'):
                        Reader(19)

                flag=flag+1

        global variableCount
        variableCount= flag
        print('Total number of Food Items Selected= ', variableCount)
        print('Therefore, number of variables= ', variableCount)
        constSequencing()
        return variableCount
def Intake():
        clear()
        logo()
        protienIntake= float(input("Enter the required Daily Protien Intake: "))
        tempInp= input('L for <= and G for >= ')
        if tempInp == 'G' or 'g' :
                protein= 'G'  
        elif(tempInp=='L'):
                protein= 'L'
        else:
                print('Please enter a correct choice')
        proteinConst.append(protein)
        proteinConst.append(protienIntake)
        carbsIntake= float(input("Enter the required Daily Carbohydrate Intake: "))
        tempInp= input('L for <= and G for >= ')
        if tempInp == 'G' or 'g' :
                carbs= 'G' 
        elif(tempInp=='L'):
                carbs= 'L'
        carbsConst.append(carbs)
        carbsConst.append(carbsIntake)
        fatIntake= float(input("Enter the required Daily Fat Intake: "))
        tempInp= input('L for <= and G for >= ')
        if tempInp == 'G' or 'g' :
                fat= 'G' 
        elif(tempInp=='L'):
                fat= 'L'
        fatConst.append(fat)
        fatConst.append(fatIntake)
        calorieIntake= float(input("Enter the required Daily Calorie Intake: "))
        tempInp= input('L for <= and G for >= ')
        if tempInp == 'G' or 'g' :
                calorie= 'G' 
        elif(tempInp=='L'):
                calorie= 'L'
        calorieConst.append(calorie)
        calorieConst.append(calorieIntake)
        intakeArray= np.array([protienIntake,carbsIntake,fatIntake,calorieIntake])
        print("Total Intake Array: \n", intakeArray)
        return proteinConst,carbsConst,fatConst,calorieConst
        

#FoodChoices()
#Intake()

#Cost

def DietOptimization():
        FoodChoices()
        print(proteinConst)
        m = gen_matrix(variableCount,4)
        Intake()
        constrain(m,'2,3,4,G,23')
        constrain(m,'2,3,4,G,23')
        constrain(m,'2,3,4,G,23')
        constrain(m,'2,3,4,G,23')
        obj(m,'2,7,2,3,0')
        print(minz(m))

if __name__=='__main__':
        DietOptimization()
