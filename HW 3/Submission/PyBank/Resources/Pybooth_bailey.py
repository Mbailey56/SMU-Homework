import csv
csvpath = "Resources\election_data.csv"
# dictionary with candidates as keys and votes as values
candidates = dict()

# read the data file
with open("Resources\election_data.csv", mode="r") as csv_file:
    elections_data = csv.reader(csv_file, delimiter=',')
    next(elections_data) # skip the header
    for row in elections_data: # iterate over all rows
        candidate = row[2] # candidate name
        # if candidate name is not in the dictionary, update the dictionary 
        if candidate not in candidates.keys():
            candidates.update({candidate:0})
        # increment the number of votes by one
        candidates[candidate] += 1

        
total_votes = sum(candidates.values())
winner = max(candidates, key=lambda k: candidates[k])

# write results
file_to_output = "resultsPoll.txt"

with open(file_to_output, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Total Votes:", total_votes, "\n")
    txt_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        votes_percent = 100*votes/total_votes
        txt_file.write("{0:s}:{1: 2.3f}% ({2})\n".format(candidate, votes_percent, votes))
    txt_file.write("-------------------------\n")
    txt_file.write("Winner:", winner, "\n")
    txt_file.write("-------------------------\n")

