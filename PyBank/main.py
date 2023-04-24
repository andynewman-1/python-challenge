#Import os module
import os
#Import csv module
import csv

#define the path to csv file

#The method below does not work for me. Repeated attempts from instructor and TA are unable to understand why.
#csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

#Define path directly on my drive
csvpath = 'D:/Uni/python-challenge/PyBank/Resources/budget_data.csv'

# Define variables to hold data
total_months = 0
total_profit = 0
previous_profit = 0
current_profit = 0
profit_change = 0
profit_changes = []
months = []

#Read csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip header row
    next(csvreader)
    
    #Loop through rows in csvreader
    for row in csvreader:
        #Count total number of months
        total_months += 1
        
        #Calculate total profit/loss
        current_profit = int(row[1])
        total_profit += current_profit
        
        #Change in profit/loss and add to list of changes
        if total_months > 1:
            profit_change = current_profit - previous_profit
            profit_changes.append(profit_change)
            months.append(row[0])
        
        #Set previous profit/loss
        previous_profit = current_profit
    
    #Average change in profit/loss
    avg_change = sum(profit_changes) / len(profit_changes)
    
    #Greatest increase and decrease in profits
    greatest_increase = max(profit_changes)
    greatest_decrease = min(profit_changes)
    max_month = months[profit_changes.index(greatest_increase)]
    min_month = months[profit_changes.index(greatest_decrease)]
    
    #Print results
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit}")
    print(f"Average Change: ${round(avg_change, 2)}")
    print(f"Greatest Increase in Profits: {max_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})")

    #Export to a text file
output_file = 'D:/Uni/python-challenge/PyBank/analysis/financial_analysis.txt'
with open(output_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Months: {total_months}\n")   
    outfile.write(f"Total: ${total_profit}\n")
    outfile.write(f"Average Change: ${round(avg_change, 2)}\n")
    outfile.write(f"Greatest Increase in Profits: {max_month} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {min_month} (${greatest_decrease})\n")
    
