expenseslist = [2200,2300,2600,2130,2190]

extraespenses = expenseslist[1]-expenseslist[0]
print(extraespenses)
totalcost = expenseslist[0]+expenseslist[1]+expenseslist[3]
print(totalcost)

for i in range(0,len(expenseslist)):
    if expenseslist[i] == 2000:
        print("yes")

expenseslist.append(1980)
print(expenseslist)

n = int(input("enter max num"))
A=[]
for  i in range(0,n):
    if i%2!=0:
        A.append(i)

print(A)