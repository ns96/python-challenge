#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Main script for python challege -- PyPoll 

Created on Wed Aug 30 18:13:18 2023

@author: Nathan Stevens
"""
import os
import csv

# set the file path to the budget data csv file
election_data_csv = os.path.join("Resources", "election_data.csv")

# set the file path to the text file which stores the analysis
analysis_txt = os.path.join("analysis", "analysis.txt")

# define dictionary to hold election results
candidate_info = dict()

# print out and save the analysis to a text file
def print_analysis():
    max_votes = 0
    winner = ''
    
    summary = "\nElection Results\n\n"
    summary += "-" * 50 + "\n\n"
    summary += "Total Votes: " + str(total_votes) + "\n\n"
    summary += "-" * 50 + "\n\n\n"
    
    # get the candiates and their votes
    for candidate in candidate_info:
        candidate_vote = candidate_info[candidate]
        candidate_percent = float(candidate_vote/total_votes)
        
        summary += candidate + ": " + "{:.3%}".format(candidate_percent) 
        summary += " (" + str(candidate_vote) + ")\n\n"
        
        # based on votes see if this candidate is the winner
        if candidate_vote > max_votes:
            max_votes = candidate_vote
            winner = candidate
    
    summary += "-" * 50 + "\n\n"
    summary += "Winner: " + winner + "\n\n"
    summary += "-" * 50 + "\n"
    
    print(summary)
    
    # save the summary to a text file now
    with open(analysis_txt, 'w') as outfile:
        outfile.write(summary)


# function to process the election csv file
def process_election():
    global total_votes
    
    # keep track of total votes
    total_votes = 0
    
    # Read in the CSV file and store candidates and keep track of vote count
    with open(election_data_csv, 'r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # read the header
        next(csvreader)
        
        # Loop through the data and store candidate and their vote count data
        # in a dictionary
        for row in csvreader:
            candidate = row[2]
            
            # check to see if the candidate is already in the dictionary,
            # otherwise add them and 1 vote for them. If they are in dictionary 
            # then just increment their vote count by 1
            if candidate not in candidate_info.keys():
                candidate_info[candidate] = 1
            else:
                candidate_info[candidate] += 1
            
            total_votes += 1
            
        # print and save the analysis
        print_analysis()

# define the main function
if __name__ == "__main__":
    process_election()
