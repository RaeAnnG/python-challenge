# import the os module
import os

# import Module for reading CSV files
import csv

# import Pandas
import pandas as pd

# read file
election_data_file = os.path.join('Resources', 'election_data.csv')

# reading Method using CSV module
Total_Votes = 0
WinningVote = 0
WinningCandidate = " "

CandidateList =[] 
CandidateVotes = {}
CandidateVoteTotal = {}
CandidateVoteTotal = []
CandidateVotePercentage = []
CandidateVoteList = []

with open(election_data_file, encoding="utf-8") as csvfile:
    # specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
#print(csvreader)
    csv_header = next(csvreader) 
    # For loop for calculations
    for row in csvreader:
        Total_Votes = Total_Votes + 1
        CandidateName = row[2]
        if CandidateName not in CandidateList:
            CandidateList.append(CandidateName)
            CandidateVotes[CandidateName] = 0
        CandidateVotes[CandidateName] = CandidateVotes[CandidateName] + 1

#output file
pypoll_txt = os.path.join('Resources','pypoll.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
with open(pypoll_txt, "w") as textfile:

    #assign Title and line break
    title =(f"Election Results\n")
    line = (f"---------------------\n")

    #print Header Election Results
    print(title)
    textfile.write(title)

    #print line break
    print (str(line))
    textfile.write(str(line))

    print("Total Votes: " + str(Total_Votes) +"\n")

    TotalVotes = (
    f"\n\nTotal Votes: {Total_Votes}\n"
    f"Total Votes:{Total_Votes}\n")  

    textfile.write("Total Votes: " + str(Total_Votes)  +"\n")



    #print line break
    print (str(line))
    textfile.write(str(line))

    for CandidateVoteTotal in CandidateVotes:
        Votes = CandidateVotes.get(CandidateVoteTotal) 

        CandidateVotePercentage = float(Votes) / float(Total_Votes) * 100

        #Winning Candidate
        if WinningVote < Votes:
            WinningVote = Votes
            WinningCandidate = CandidateVoteTotal
        output = f"{CandidateVoteTotal}: {CandidateVotePercentage:.3f}% ({Votes})\n"
        print(output)
        textfile.write(output)
        print (str(line))
        textfile.write(str(line))
   
    print(f"Winner: {WinningCandidate}\n")
    
    textfile.write("Winner: " + WinningCandidate)
    print (str(line))
    

    