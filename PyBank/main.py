#Import specific CSV file
import os
import csv
csvpath = os.path.join("Resources", "budget_data.csv")


#Create empty string and variables
month = []
total_amount = 0
running_total = 0
previous_amount = 0
difference = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = 0
greatest_decrease_month = 0


#Open the CSV file           
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   #iterate through the CSV file
    for row in csvreader:
        #Zip the month list
        month.append(row[0])
        total_amount += int(row[1])
        
        #calculate the difference
        if previous_amount != 0:
            difference = ((int(row[1]))-(previous_amount))
        
        #store the greatest increase
        if difference > greatest_increase:
            greatest_increase = difference
            greatest_increase_month = (row[0])

        #store the greatest decrease
        if difference < greatest_decrease:
            greatest_decrease = difference
            greatest_decrease_month = (row[0])
        
        #calculate the running total
        running_total += difference           
       
       #set the previous amount for the next equation
        previous_amount = int(row[1])  
    
    #calculate the average change
    average_change = round((running_total/85),2)

#print the outcome    
print("Financial Analysis")
print("-----------------------------------")

print(f"Total Months: {len(month)}")
print(f"Total: ${total_amount}")
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

#print the outcome to a txt file
file_path = "PyBank\\analysis\\output.txt"

with open(file_path, 'w') as file:
    file.write("Financial Analysis\n"
    "-----------------------------------\n"

    f"Total Months: {len(month)}\n"
    f"Total: ${total_amount}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
