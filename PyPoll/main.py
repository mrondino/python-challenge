#Import specific CSV file
import os
import csv
csvpath = os.path.join("Resources", "election_data.csv")


#Create empty string and variables
votes = []
CCS_List = []
CCS_Percent = 0
CCS_Total = 0
DD_List = []
DD_Percent = 0
DD_Total = 0
RAD_List = []
RAD_Percent = 0
RAD_Total = 0
Winner = 0

#Open the CSV file           
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   #iterate through the CSV file
    
    #count votes for each candidate
    for row in csvreader:
        votes.append(row[0])
        if row[2] == "Charles Casper Stockham":
            CCS_List.append(row[2])
        if row[2] == "Diana DeGette":
            DD_List.append(row[2])
        if row[2] == "Raymon Anthony Doane":
            RAD_List.append(row[2])

    #calculate candidate percentage by dividing by total votes
    CCS_Percent = round((((len(CCS_List))/(len(votes)))*100),3)
    DD_Percent = round((((len(DD_List))/(len(votes)))*100),3)
    RAD_Percent = round((((len(RAD_List))/(len(votes)))*100),3)

    #compare to see who is the winner
    if CCS_Percent > DD_Percent and RAD_Percent:
        Winner = "Charles Casper Stockham"

    if DD_Percent > CCS_Percent and RAD_Percent:
        Winner = "Diana DeGette"

    if RAD_Percent > DD_Percent and CCS_Percent:
        Winner = "Raymon Anthony Doane"

#print the outcome    
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {len(votes)}")
print("-----------------------------------")
print(f"Charles Casper Stockham: {CCS_Percent}% ({len(CCS_List)})")
print(f"Diana DeGette: {DD_Percent}% ({len(DD_List)})")
print(f"Raymon Anthony Doane: {RAD_Percent}% ({len(RAD_List)})")
print("-----------------------------------")
print(f"Winner: {Winner}")
print("-----------------------------------")

#print the outcome to a txt file
file_path ="PyPoll\\analysis\\output.txt"

with open(file_path, 'w') as file:
    file.write("Election Results\n"
        "-----------------------------------\n"   
        f"Total Votes: {len(votes)}\n"
        "-----------------------------------\n"
        f"Charles Casper Stockham: {CCS_Percent}% ({len(CCS_List)})\n"
        f"Diana DeGette: {DD_Percent}% ({len(DD_List)})\n"
        f"Raymon Anthony Doane: {RAD_Percent}% ({len(RAD_List)})\n"
        "-----------------------------------\n"
        f"Winner: {Winner}\n"
        "-----------------------------------\n")
