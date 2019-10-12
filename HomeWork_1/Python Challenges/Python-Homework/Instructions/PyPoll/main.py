# Import Modules
import os
import csv


# Variables
vote_total = 0
vote_khan = 0
vote_correy = 0
vote_li = 0
vote_otooley = 0

# Setting path for CVS file

csv_path = os.path.join('..', 'PyPoll', 'Resources', 'election_data.csv')

# Reading CSV file

with open(csv_path, newline='') as csv_file:

    #Specify delimiter & variable 
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    # Read the header row first 
    csv_header = next(csv_file)

    # Read each row Of data after the header
    for row in csv_reader:
        
        # Calculate total votes casted
        vote_total += 1
        
        # Calculate total number Of votes each candidate won
        if (row[2] == "Khan"):
            vote_khan += 1
        elif (row[2] == "Correy"):
            vote_correy += 1
        elif (row[2] == "Li"):
            vote_li += 1
        else:
            vote_otooley += 1
    # Calculate percentage Of votes each candidate won
    percent_khan = vote_khan / vote_total
    percent_correy = vote_correy / vote_total
    percent_li = vote_li / vote_total
    percent_otooley = vote_otooley / vote_total

    # Calculate Winner Of election based on popular vote
    vote_winner = max(vote_khan, vote_correy, vote_li, vote_otooley)

    if vote_winner == vote_khan:
        winner = "Khan"
    elif vote_winner == vote_correy:
        winner = "Correy"
    elif vote_winner == vote_li:
        winner = "Li"
    else:
        winner = "O'Tooley" 

# Print Analysis
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {vote_total}")
print(f"---------------------------")
print(f"Kahn: {percent_khan:.3%}({vote_khan})")
print(f"Correy: {percent_correy:.3%}({vote_correy})")
print(f"Li: {percent_li:.3%}({vote_li})")
print(f"O'Tooley: {percent_otooley:.3%}({vote_otooley})")
print(f"---------------------------")
print(f"Winner: {winner}")
print(f"---------------------------")

# Specify File To Write To
output_file = os.path.join('..', 'PyPoll', 'Resources', 'election_data_revised.text')

# Open File Using "Write" Mode. Specify The Variable To Hold The Contents
with open(output_file, 'w',) as txtfile:

# Write New Data
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {vote_total}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {percent_khan:.3%}({vote_khan})\n")
    txtfile.write(f"Correy: {percent_correy:.3%}({vote_correy})\n")
    txtfile.write(f"Li: {percent_li:.3%}({vote_li})\n")
    txtfile.write(f"O'Tooley: {percent_otooley:.3%}({vote_otooley})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write(f"---------------------------\n")