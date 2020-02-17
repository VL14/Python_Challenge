import os
import csv

# Path to collect data from the Pybank folder
pybank_csv = os.path.join('..', 'Pybank', 'budget_data.csv')

#Set initial value for count variable
count = 0

#Loop through file and count number of rows
with open(pybank_csv, 'r') as csvfile:
    for row in csvfile:
        count += 1

#Store count to print and export late
rowcount = (count-1)

# Determine total amount of profit/loss
with open(pybank_csv, 'r') as csvfile:

    #Set initial value for sum variable
    totalprofit = 0

    #Define the delimiter for each line
    column = csvfile.readline().split(',')

    #Run through file and sum all profits/losses
    for column in csv.reader(csvfile):
        conv_int = int(column[1])
        totalprofit = (totalprofit + conv_int)
    
    print(totalprofit)
    
    #Calculate average daily change
    Averagechange = round((totalprofit / rowcount),2)
    print(Averagechange)

    #Determine date and amount of greatest increase in profits
    profit = []

    for column in csv.reader(csvfile):
        profit.append(int(column[1]))
        
    print(profit)
    #print ("min value : ", min(profit))
    #print ("max value : ", max(profit)) 