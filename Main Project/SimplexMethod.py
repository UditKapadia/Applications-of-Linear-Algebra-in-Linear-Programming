import numpy as np 
from fractions import Fraction as f 

# Input and Table formation 

n_variable=int(input("Enter the number of variables:")) #no. of variables
n_equation = int(input("Enter the number of  equations:")) #no. of equations

#Coeficient of Objective function
print("Enter the maximizing equation coefficient separated by space: ") 
obj_fun=list(map(float,input().split()))
print(obj_fun)
for i in range(n_equation):
    obj_fun.append(float(0))
print(obj_fun)    

# Basic variable column
B=list()
coefficient_matrix=list()

#Cost of Basic variable matrix
CB=list()   
constraint=[]

# Coefficient Matrix
print("Enter the equations coefficient separated by space: e.g (a*x1 + b*x2 +c*x3 >= d, then write a b c d)")
for i in range(n_equation):
    entries=list(map(float,input().split()))
    constraint.append(entries.pop(-1)) 
    coefficient_matrix.append(entries)
A =np.array(coefficient_matrix)  

print(constraint)
print(A)


#Making of tableu
for i in range(n_equation):
    CB.append(0)
    B.append(i+n_variable)
CB= np.array(CB)
CB=np.transpose([CB])
c= np.array(obj_fun)
c=np.transpose([c])  
B = np.array(B)
B=np.transpose([B]) 
tableu = np.hstack((B, CB))
tableu = np.hstack((tableu, A))
slack=np.identity(n_equation)
tableu=np.append(tableu,slack,axis=1)
constraint=np.transpose([constraint])
tableu = np.hstack((tableu, constraint))
tableu = np.array(tableu, dtype ='float')

#Minimum Theta Calculation
def pivot_test(tableu,col_index):
    t=0
    row_index=0
    i=0
    minimum=99999
    l=list(tableu[:,col_index])
    while i < n_equation:
        if l[i] != 0.0:
            value=tableu[i,2+n_variable+n_equation]/l[i] 
            if value >= 0:
                if minimum > value:
                    minimum= value
                    row_index=i
                    t=1
        i=i+1
    return row_index,t

# Table display and Iteration
s=""
itr=0
for i in range(n_equation+n_variable):
    s=s+("\tx" +str(i+1))   
while True: 
    itr=itr+1
    print("Table iteration: " + str(itr)) 
    print("B \tCB "+s+" \tRHS")
    i=0
    for row in tableu:
        for element in row:
            if i%(n_equation+n_variable+3)== 0:
                print('x'+str(int(element)+1), end ='\t')  
            else:
                print(f(str(element)).limit_denominator(100), end ='\t') 
            i=i+1
        print() 
    print()
    i=0

    maximize=[]
    theta=[]
    while i<len(obj_fun):
        maximize.append(obj_fun[i] - np.sum(tableu[:, 1]*tableu[:, 2 + i]))
        i = i + 1 
    print("maximize",end='\t')
    for element in maximize: 
            print(f(str(element)).limit_denominator(100), end ='\t')  
    if max(maximize)<=0:
        break
    col_index=maximize.index(max(maximize))+2
    row_index,t=pivot_test(tableu,col_index)
    if t==0:
        print("Unboundedness occured")
        break
    pivot=tableu[row_index,col_index]
    tableu[row_index, 2:n_equation+5] = tableu[row_index, 2:n_equation+5] / pivot
    i=0
    while i<n_equation:
        if i != row_index:
            tableu[i, 2:n_equation+5] = tableu[i,2:n_equation+5] - tableu[i][col_index]*tableu[row_index][2:n_equation+5]
        i=i+1
     # Assign the new basic variable 
    tableu[row_index][0] = col_index-2 
    tableu[row_index][1] = obj_fun[col_index-2]
    print() 
    print()
# Alternate Solution
if not np.any(tableu[:,0]== 0):
    col_index=2
elif not np.any(tableu[:,0]== 1):
    col_index=3
else:
    col_index=-1
if (col_index == 2 or col_index == 3):
    row_index,t=pivot_test(tableu,col_index)
    pivot=tableu[row_index,col_index]
    tableu[row_index, 2:n_equation+5] = tableu[row_index, 2:n_equation+5] / pivot
    i=0
    while i<n_equation:
        if i != row_index:
            tableu[i, 2:n_equation+5] = tableu[i,2:n_equation+5] - tableu[i][col_index]*tableu[row_index][2:n_equation+5]
        i=i+1
    # Assign the new basic variable 
    tableu[row_index][0] = col_index-2 
    tableu[row_index][1] = obj_fun[col_index-2]
    print("\n\n \t\t Alternate Solution")
    itr=itr+1
    print("Table iteration: " + str(itr)) 
    print("B \tCB "+s+" \tRHS")
    i=0
    for row in tableu:
        for element in row:
            if i%(n_equation+n_variable+3)== 0:
                print('x'+str(int(element)+1), end ='\t')
            else:
                print(f(str(element)).limit_denominator(100), end ='\t')
            i=i+1
        print() 
    print()
    print() 
    print()
# Maximum  Possible Value 
Z= np.sum(tableu[:, 1]*tableu[:,n_equation+n_variable+2])
print("Maximum Z= ",Z)