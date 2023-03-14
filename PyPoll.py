#import dependencies
import pandas as pd

#read data from csv
election_data = "Starter_Code (8)/Instructions/PyPoll/Resources/election_data.csv"
election_data_df = pd.read_csv(election_data)

#create and assign variable to calculate total number of votes cast
total_votes = len(election_data_df)

#Create and assign variable for the list of candidates that recieved votes
candidates_list = election_data_df["Candidate"].unique()

#Create a series to hold the total number of votes cast for each candidate
vote_results = election_data_df["Candidate"].value_counts()

#Create and assign variables for candidates name, total votes earned, and percent of votes
# for the winner, second place, and third place candidates
winner = vote_results.index[0]
winner_votes = vote_results[0]
winner_votes_percentage = round((winner_votes/total_votes)*100, 3)

second_place = vote_results.index[1]
second_place_votes = vote_results[1]
second_place_votes_percentage = round((second_place_votes/total_votes)*100, 3)

third_place = vote_results.index[2]
third_place_votes = vote_results[2]
third_place_votes_percentage = round((third_place_votes/total_votes*100), 3)

#Create a election analysis variable to store text and format variables
election_analysis = f'''Election Analysis\n\
-------------------------
Total Votes: {total_votes}
-------------------------
{winner}: {winner_votes_percentage}% ({winner_votes})
{second_place}: {second_place_votes_percentage}% ({second_place_votes})
{third_place}: {third_place_votes_percentage}% ({third_place_votes})
-------------------------
Winner: {winner}
-------------------------'''

#print election analysis
print(election_analysis)

#export election analysis as PyPoll.txt file
file = open("PyPoll.txt", "w")
file.writelines(election_analysis)
file.close()