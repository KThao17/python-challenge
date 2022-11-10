import os
import csv

election_csv = 'Starter_Code\Instructions/PyPoll\Resources/election_data.csv'

total_votes = 0 
votes_per_candidate = {}

with open(election_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in votes_per_candidate:
            votes_per_candidate[row[2]] = 1
        else:
            votes_per_candidate[row[2]] += 1   
        
        


f = open("election_analysis.txt", "w")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

for candidate, votes in votes_per_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")