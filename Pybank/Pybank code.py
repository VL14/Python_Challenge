import os
import csv

# Path to collect budget data
pybank_csv = os.path.join('..', 'Pybank', 'budget_data.csv')

#Set initial value for count variable
count = 0

#Loop through file and count number of rows
with open(pybank_csv, 'r') as csvfile:
    for row in csvfile:
        count += 1

#Store count to print and export later
rowcount = (count-1)

# Determine total amount of profit/loss
with open(pybank_csv, 'r') as csvfile:

    #Set initial value for sum variable
    totalprofit = 0

    #Define the delimiter for each line
    column = csvfile.readline().split(',')
    
    #Create an array to hold all profits for finding the max and min
    profits=[]

    #Run through file to sum all profits/losses and populate profits array
    for column in csv.reader(csvfile):
        monthlyprofit = int(column[1])
        profits.append(int(column[1]))
        totalprofit = (totalprofit + monthlyprofit)
    
    #Calculate average daily change
    Averagechange = round((totalprofit / rowcount),2)
    
#Create output header
header_string = 'Financial Analysis\n--------------------\n'  

#Convert newlines to newlines+carriage return
header_string = header_string.replace('\n','\r\n') 

#Create financial summary output
summary_string1 = "Total Months: " + str(rowcount)
summary_string2 = "Total: $" + str(totalprofit)
summary_string3 = "Average Change: $ " + str(Averagechange)
summary_string4 = "Greatest Increase in Profits: $"
summary_string5 = "Greatest Decrease in Profits: $"

#Send financial summary to output file
with open('output.csv', 'w', newline = '') as outfile:
      w = csv.writer(outfile)                          
      w.writerow([header_string])   
      w.writerow([summary_string1])
      w.writerow([summary_string2])
      w.writerow([summary_string3])
      w.writerow([summary_string4])
      w.writerow([summary_string5])
    
#Print to screen
print("\nFinancial Analysis\r")
print('-'*20)
print(f"\rTotal Months: {rowcount}\r")
print(f"Total profit: ${totalprofit}\r")
print(f"Average Change: ${Averagechange}\r")
print (f"Greatest Increase in Profits : ", max(profits))
print (f"\rGreatest Decrease In Profits : ", min(profits))
