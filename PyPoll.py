    # The data we need to retrieve.
    # 1. The total number of votes cast
    # 2. A complete list of candidates who received votes
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on popular vote.

    # Resources/election_results.csv

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
 
    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
   
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row[0])
# Close the file.
election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # Write three counties to the file.
    txt_file.write("Counties in the Election\n---\nArapahoe\nDenver\nJefferson")