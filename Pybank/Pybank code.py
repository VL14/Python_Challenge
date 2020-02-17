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

#Set initial value for sum variable
totalprofit = 0

# Determine total amount of profit/loss
with open(pybank_csv, 'r') as csvfile:

    #Assign variables to each column for readability within code
    #date = date(budget_data[0])
    #profit_loss = int(row[1])
    
    # Skip the column names
    csvfile.readline()

    # Split the current line into a list: line
    column = csvfile.readline().split(',')

    #Run through file and sum all profits/losses
    for row in csvfile:
        totalprofit = (totalprofit + int(column[1]))
        print(totalprofit)