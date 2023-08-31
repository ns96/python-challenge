#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main script for python challege -- PyBank 

Created on Wed Aug 30 07:53:41 2023

@author: Nathan Stevens
"""
import os
import csv

# set the file path to the budget data csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# set the file path to the text file which stores the analysis
analysis_txt = os.path.join("analysis", "analysis.txt")

# tuple containg 3 char months so we can check that a row contains 
# valid data and not the header, or blank lines. Maybe overkill for this dataset
months_of_year = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

# function to printout and save the analysis to a text file
def print_analysis():
    summary = "\nFinancial Analysis\n"
    summary += "-" * 50 + "\n\n\n"
    summary += "Total Months: " + str(total_months) + "\n\n"
    summary += "Total: $" + str(net_total) + "\n\n"
    summary += "Average Change: $" + "{:.2f}".format(average_change) + "\n\n"
    summary += "Greatest Increase in Profits: " + max_increase_text + "\n\n"
    summary += "Greatest Decrease in Profits: " + max_decrease_text + "\n"
    
    print(summary)
    
    # save the summary to a text file now
    with open(analysis_txt, 'w') as outfile:
        outfile.write(summary)
    
# function to process the budget file
def process_budget():
    # make variables global so they can be accesses in the print_analyis function
    global total_months, net_total, average_change, max_increase_text, max_decrease_text   
    
    profit_loss_months = [] # store the months
    profit_loss = []        # store the profit/loss values
      
    # Read in the CSV file and store months profit/loss values
    with open(budget_csv, 'r') as csvfile:
        # Split the data on commas
        csvreader = csv.reader(csvfile, delimiter=',')
        
        # Loop through the data and store prices_loses data
        for row in csvreader:
            
            # grab the month so we can check if row has valid data
            month = row[0].split('-')[0]
            if month in months_of_year:
                profit_loss_months.append(row[0])
                profit_loss.append(int(row[1]))
                
        # get the net total over the entire period
        total_months = len(profit_loss_months)
        net_total = sum(profit_loss)
        
        # calculate the profit/loss changes over a period, (i.e. a month)
        # store them in a list then take average
        profit_loss_changes = []
        for i in range(1, total_months):
            profit_loss_changes.append(profit_loss[i] - profit_loss[i-1])
        
        # get the average of the profit/loss changes
        average_change = sum(profit_loss_changes)/len(profit_loss_changes)
        
        # get the maximum profit increase and store it
        max_profit_increase = max(profit_loss_changes)
        idx = profit_loss_changes.index(max_profit_increase) + 1
        max_increase_text = profit_loss_months[idx] + " ($" + str(max_profit_increase) + ")"
        
        # get the maximim profit decrease and store it
        max_profit_decrease = min(profit_loss_changes)
        idx = profit_loss_changes.index(max_profit_decrease) + 1
        max_decrease_text = profit_loss_months[idx] + " ($" + str(max_profit_decrease) + ")"
        
        # print and save the analysis
        print_analysis()

# define the main function
if __name__ == "__main__":
    process_budget()