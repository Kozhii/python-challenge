import csv

# Path to the CSV file
csv_path = "PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner_votes = 0
winner_name = ""

# Read the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    csv_header = next(csvreader)
    
    # Iterate through each row
    for row in csvreader:
        # Count total number of votes
        total_votes += 1
        
        # Get the candidate's name
        candidate = row[2]
        
        # Add candidate to the dictionary if not already present
        if candidate not in candidates:
            candidates[candidate] = 0
        
        # Increment the candidate's vote count
        candidates[candidate] += 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
    
    # Check for the winner
    if votes > winner_votes:
        winner_votes = votes
        winner_name = candidate

print("-------------------------")
print(f"Winner: {winner_name}")
print("-------------------------")

# Save the election results to a text file
output_path = "PyPoll/analysis/results.txt"
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    
    # Write the percentage of votes each candidate won
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write("-------------------------\n")

print("Analysis complete. Results saved to 'PyPoll/analysis/results.txt'.")
