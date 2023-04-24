#import os module
import os
#import csv module
import csv

#Path to election data file
#The method below does not work for me. Repeated attempts from instructor and TA are unable to understand why.
#csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Define path directly on my drive
csvpath = 'D:/Uni/python-challenge/PyPoll/Resources/election_data.csv'

#Set variables
total_votes = 0
candidate_votes = {}
winner_votes = 0
winner = ""

#Read the csv file
with open(csvpath,) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    #Loop through each row of data
    for row in csvreader:
        total_votes += 1
        candidate = row[2]

        #If the candidate not in the dictionary, add them with 0 votes
        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0

        #Add vote to the candidate total
        candidate_votes[candidate] += 1

#Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_pct = round(votes / total_votes * 100, 3)
    print(f"{candidate}: {vote_pct}% ({votes})")
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Export to a text file
output_file = 'D:/Uni/python-challenge/PyPoll/analysis/election_results.txt'
with open(output_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_pct = round(votes / total_votes * 100, 3)
        outfile.write(f"{candidate}: {vote_pct}% ({votes})\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")
