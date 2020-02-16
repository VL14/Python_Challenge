import os
import csv

# Path to collect data from the Pybank folder
pybank_csv = os.path.join('..', 'Pybank', 'budget_data.csv')

#Set initial amount for count variable
count = 0

with open(pybank_csv, 'r') as f:
    for line in f:
        count += 1

#print ("There are " + str(count-1) + " number of data rows" )

#Assign variables to each column for readability within code
#date = date(budget_data[0])
#profit_loss = int(budget_data[1])

# Loop through looking for the video
    #for row in csvreader:
        #if row[0] == video:
            #print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])