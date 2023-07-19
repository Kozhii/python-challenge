import csv

# Path to the CSV file
csv_path = "PyBank/Resources/budget_data.csv"

# Initializing variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_increase_date = ""
greatest_decrease = 0
greatest_decrease_date = ""

# Reading the CSV file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip header row
    csv_header = next(csvreader)
    
    # Iterate through each row
    for row in csvreader:
        # Count total number of months
        total_months += 1
        
        # Calculating net total amount
        profit_loss = int(row[1])
        net_total += profit_loss
        
        # Calculating change in profit/loss
        if previous_profit_loss != 0:
            change = profit_loss - previous_profit_loss
            total_change += change
            
            # Checking for greatest increase and decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]
        
        # Updating previous profit/loss
        previous_profit_loss = profit_loss

# Calculating average change
average_change = total_change / (total_months - 1)

# Printing the analysis results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Saving the analysis results to a text file
output_path = "PyBank/analysis/results.txt"
with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("---------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${net_total}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

print("Analysis complete. Results saved to 'PyBank/analysis/results.txt'.")
