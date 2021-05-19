from pulp import *
import numpy as np


n_items=int(input("No. of Items produced:"))
n_resources=int(input("No. of resources/materials used to make item:"))

print("Write profit per item:")
items = []
for i in range(n_items):
    print("Item",i+1,":")
    items.append(float(input()))
my_array = np.array(items)
print(np.floor(items))

print("Write maximum no. of resources can be used:")
constarints = []
for i in range(n_resources):
    print("Maximum no. of resource",i+1, " can be used :")
    constarints.append(float(input()))
my_array1 = np.array(constarints)
print(np.floor(constarints))

print(("No. of resources used per item:"))
cost_matrix=[]
for i in range(n_resources):
    cost_matrix.append([])
for i in range(n_resources):
    for j in range(n_items):
        print("Resource ",i+1, "for item ",j+1, ":")
        cost_matrix[i].append(float(input()))

my_array3=np.array(cost_matrix)

model = LpProblem("Profit_Maximization", LpMaximize)

if n_items==2 :
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)
    obj_fun=x*my_array[0]+y*my_array[1]

    for i in range(n_resources):
    
        model+=(x*my_array3[i][0] + y*my_array3[i][1] <= my_array1[i])
        

    
    model+=obj_fun
    print(model)
    status = model.solve()
   
    print("x=",x.value())
    print("y=",y.value())
    print("Maximum Profit",model.objective.value())

elif n_items==3:
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)
    z = LpVariable(name="z",lowBound=0)
    obj_fun=x*my_array[0]+y*my_array[1]+z*my_array[2]

    for i in range(n_resources):
    
        model+=(x*my_array3[i][0] + y*my_array3[i][1]  + z*my_array3[i][2] <= my_array1[i])
        

    model+=obj_fun
    print(model)
    status = model.solve()
    print(status)
    print("x=",x.value())
    print("y=",y.value())
    print("z=",z.value())
    print("Maximum Profit",model.objective.value())

elif n_items==4:
    x = LpVariable(name="x", lowBound=0)
    y = LpVariable(name="y", lowBound=0)
    z = LpVariable(name="z",lowBound=0)
    t = LpVariable(name="t",lowBound=0)

    obj_fun = x*my_array[0] + y*my_array[1] + z*my_array[2] + t*my_array[3]

    for i in range(n_resources):
    
        model+=(x*my_array3[i][0] + y*my_array3[i][1]  + z*my_array3[i][2] + t*my_array3[i][3] <= my_array1[i])
        
    
    model+=obj_fun
    print(model)
    status = model.solve()
 
    print("x=",x.value())
    print("y=",y.value())
    print("z=",z.value())
    print("t=",t.value())
    print("Maximum Profit",model.objective.value())

elif n_items==5:
    p = LpVariable(name="r", lowBound=0)
    q = LpVariable(name="q", lowBound=0)
    r = LpVariable(name="r",lowBound=0)
    s = LpVariable(name="s",lowBound=0)
    t = LpVariable(name="t",lowBound=0)

    obj_fun = p*my_array[0] + q*my_array[1] + r*my_array[2] + s*my_array[3] + t*my_array[4]

    for i in range(n_resources):
    
        model+=(p*my_array3[i][0] + q*my_array3[i][1]  + r*my_array3[i][2] + s*my_array3[i][3] + t*my_array3[i][4] <= my_array1[i])
        print(model)

    model+=obj_fun
    print(model)
    status = model.solve()
    print(status)
    print("p=",p.value())
    print("q=",q.value())
    print("r=",r.value())
    print("s=",s.value())
    print("t=",t.value())
    print("Maximum Profit",model.objective.value())


else:
    print("System is limited for only 5 variables..")