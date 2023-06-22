# import modules
import os
import csv

csvpath = os.path.join('..','PyPoll', 'Resources', 'election_data.csv')

output = os.path.join('..', 'PyPoll', 'Analysis', 'analysis.txt')

#initialize variables
counter = 0
candidates = []
votes = 0
votesCount = []
votesPercent = []
percent = 0
winningVote = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    for row in csvreader:
        counter = counter + 1
        candidates.append(row[2])

    #candidates = sorted(candidates, reverse=True)
    uniqueCandidates = set(candidates)
    uniqueCandidates = sorted(list(uniqueCandidates))  
    for candidate in uniqueCandidates:
        votes = candidates.count(candidate)

        votesCount.append(votes)
        percent = (votes/counter)*100

        votesPercent.append(percent)

    
    winningVote = max(votesCount)
    winner = uniqueCandidates[votesCount.index(winningVote)]
    votesPercent = [round(x,3) for x in votesPercent]


with open('analysis.txt', "w") as text:
    text.write("Election Results \n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(counter) + "\n")
    text.write("------------------------- \n")
    text.write(str(uniqueCandidates[0]) + ": " + str(votesPercent[0]) +"% (" + str(votesCount[0]) + ")\n")
    
    text.write(str(uniqueCandidates[1]) + ": " + str(votesPercent[1]) +"% (" + str(votesCount[1]) + ")\n")
    text.write(str(uniqueCandidates[2]) + ": " + str(votesPercent[2]) +"% (" + str(votesCount[2]) + ")\n")
    text.write("-------------------------\n")
    text.write("Winner: " + str(winner) + "\n")
    text.write("-------------------------\n")

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(counter))
print("-------------------------")
print(str(uniqueCandidates[0]) + ": " + str(votesPercent[0]) +"% (" + str(votesCount[0]) + ")")
print(str(uniqueCandidates[1]) + ": " + str(votesPercent[1]) +"% (" + str(votesCount[1]) + ")")
print(str(uniqueCandidates[2]) + ": " + str(votesPercent[2]) +"% (" + str(votesCount[2]) + ")")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

