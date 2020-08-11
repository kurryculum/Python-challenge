import os
import csv

Totalvotes = 0
candidate=[]
candidatelist = []

#candidatelistDict['this is a key'] = 'this is a value'

candidate_votes = {}

unique_candidate = []
vote_count = []
vote_percent = []

election_dataFilePath =  os.path.join("../Resources/" + "election_data.csv")
#read csv
with open(election_dataFilePath, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    csv_reader = next(csvreader)
    votes =0
    candidatelist = []


    for row in csvreader: 
        Totalvotes += 1
        current_candidate = row[2]
        if current_candidate not in candidatelist:
            candidatelist.append(current_candidate)
            candidate_votes[current_candidate] = 0

        candidate_votes[current_candidate] += 1

        

# print(candidate_votes)
# print(Totalvotes)

winning_candidate=''
winning_votes=0

for candidate in candidate_votes:

    if candidate_votes[candidate] > winning_votes:
        winning_candidate = candidate
        winning_votes = candidate_votes[candidate]

    #print('percent', float(candidate_votes[candidate])/float(Totalvotes)*100)
    
# print(winning_candidate)
# print(winning_votes)


print("Election Results")
print("-------------------------")
print(Totalvotes)
print("-------------------------")
for key,value in candidate_votes.items():
    print(f"{key}:{round(value/Totalvotes,2)*100}% ({value })")

print("-------------------------")
# print(clear)


print(f"Winner: {winning_candidate}")
print("-------------------------")






with open("PyPollAnalysis.txt", "w") as analysis:
    analysis.write("Election Results\n")
    analysis.write("-------------------------\n")
    analysis.write(f"Total Votes: {Totalvotes}\n")
    analysis.write("-------------------------\n") 

    for key,value in candidate_votes.items():
        analysis.write(f"{key}:{round(value/Totalvotes,2)*100}% ({value })\n")

     # analysis.write("-------------------------\n")
    analysis.write(f"Winner: {winning_candidate}")
    