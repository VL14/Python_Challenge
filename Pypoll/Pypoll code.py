import os
import csv

# Path to collect poll data
pypoll_csv = os.path.join('..', 'Pypoll', 'election_data.csv')

#Set initial values for vote count variable
count = 0

#Create a list with all candidate's names
candidates = ["Khan", "Correy", "Li", "O'Tooley"]

#Create a list to hold count of votes per candidate
vote_count = [0,0,0,0]

#Loop through file: count number of rows and votes
with open(pypoll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip the header
    next(csvreader)
    
    for row in csvreader:
        count += 1
        
        #Pull each vote in csv
        vote = row[2]

        #Create if loop to assign index for each candidate
        if vote == "Khan":
            vote_index = 0
        elif vote == "Correy":
            vote_index = 1
        elif vote == "Li":
            vote_index = 2
        elif vote == "O'Tooley":
            vote_index =3
        else:
            print("row" + row + "has an invalid candidate")

        #Add vote to the vote count list using the index
        vote_count[vote_index] += 1     

#Store count to print and export later
totalvotes = (count-1)

#Print poll summary to screen
print (f"\nELECTION RESULTS\r")
print ("-"*20)
print (f"\rTotal votes: {totalvotes}\r")
print ("-"*20)

#Calculate number and percent of votes for each candidate and print
khan_votes = vote_count[0]
khan_percent = round((khan_votes/totalvotes*100),3)
print (f"\rKhan: {khan_percent}% ({khan_votes})")
correy_votes = vote_count[1]
correy_percent = round((correy_votes/totalvotes*100),3)
print (f"\rCorrey: {correy_percent}% ({correy_votes})")
li_votes = vote_count[2]
li_percent = round((li_votes/totalvotes*100),3)
print (f"\rLi: {li_percent}% ({li_votes})")
otooley_votes = vote_count[3]
otooley_percent = round((otooley_votes/totalvotes*100),3)
print (f"\rO'Tooley: {otooley_percent}% ({otooley_votes})")

#Calculate winner
maxvotes = max(vote_count)
winner_index = vote_count.index(maxvotes)
winner = candidates[winner_index]
print ("-"*20)
print (f"\rWinner: {winner}\r")
print ("-"*20)


