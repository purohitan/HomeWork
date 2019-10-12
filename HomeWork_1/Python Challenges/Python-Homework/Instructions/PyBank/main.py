# PyBank Financial Records
#Import Modules
import csv
import os

# Define Variables

total_amount = 0
change_monthly = []
count_month = []
total_months = 0
gr_inc = 0
gr_dec = 0
gr_inc_month = 0
gr_dec_month = 0

# Setting path for CVS file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV File

with open(csvpath, newline='') as csvfile:
    
    # Specify Delimiter & Variable 
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # Read The Header Row First 
    csv_header = next(csv_reader)
    row = next(csv_reader)
    
 # Calculate Total Months, Total Amount and set variables for rows
 
    row_previous = int(row[1])
    total_months += 1
    total_amount += int(row[1])
    gr_inc = int(row[1])
    gr_inc_month = row[0]
    
    # Reading each row after header
    for row in csv_reader:
        
        # Calculate total number of months
        total_months += 1
        # Calculate Total Amount for the entire period
        total_amount += int(row[1])

        # Calculate Change From Current Month To Previous Month
        change_revnue = int(row[1]) - row_previous
        change_monthly.append(change_revnue)
        row_previous = int(row[1])
        count_month.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > gr_inc:
            gr_inc = int(row[1])
            gr_inc_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < gr_dec:
            gr_dec = int(row[1])
            gr_dec_month = row[0]  
        
    # Calculate average and date
    average = sum(change_monthly)/ len(change_monthly)
    
    highest_value = max(change_monthly)
    lowest_value = min(change_monthly)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_amount}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits:, {gr_inc_month}, (${highest_value})")
print(f"Greatest Decrease in Profits:, {gr_dec_month}, (${lowest_value})")

#Declear file path to write data 
output_file = os.path.join('..', 'PyBank', 'Resources', 'budget_data_revised.txt')

# Open file using "Write" Mode. Specify the variable To hold The contents
with open(output_file, "w", newline="") as txt_file:

# Write New Data
    txt_file.write(f"Financial Analysis\n")
    txt_file.write(f"---------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_amount}\n")
    txt_file.write(f"Average Change: ${average}\n")
    txt_file.write(f"Greatest Increase in Profits:, {gr_inc_month}, (${highest_value})\n")
    txt_file.write(f"Greatest Decrease in Profits:, {gr_dec_month}, (${lowest_value})\n")
  



