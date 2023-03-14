#import dependencies
import pandas as pd

#read data from csv
budget_data = "Starter_Code (8)/Instructions/PyBank/Resources/budget_data.csv"
budget_data_df = pd.read_csv(budget_data)

#create and assign variables for total months and total profits/losses
total_months = len(budget_data_df)
total_profits_losses = budget_data_df["Profit/Losses"].sum()

#create new column in data frame for "Monthly Change"
budget_data_df["Monthly Change"] = 0

#Run a for loop to calculate and store values for Monthly Change
for i in range(len(budget_data_df) - 1):
    change = budget_data_df["Profit/Losses"][i + 1] - budget_data_df["Profit/Losses"][i]
    budget_data_df["Monthly Change"][i] = change

#Create and assign variables for maximum monthly change, maximum monthly change date,
# minimum monthly change, minimum monthly change date, and average Monthly Change
sorted_budget_data_df = budget_data_df.sort_values("Monthly Change", ascending=False)
greatest_increase = sorted_budget_data_df.head(1)
max_monthly_change = greatest_increase["Monthly Change"].values[0]
max_monthly_change_date = greatest_increase["Date"].values[0]
greatest_decrease = sorted_budget_data_df.tail(1)
min_monthly_change = greatest_decrease["Monthly Change"].values[0]
min_monthly_change_date = greatest_decrease["Date"].values[0]
avg_monthly_change = round(budget_data_df["Monthly Change"].sum()/(len(budget_data_df) - 1), 2)

#Create a financial analysis variable to store text and format variables
financial_analysis = f'''Financial Analysis\n\
----------------------------\n\
Total Months: {total_months}\n\
Total: ${total_profits_losses}\n\
Average Change: ${avg_monthly_change}\n\
Greatest Increase in Profits: {max_monthly_change_date} (${max_monthly_change})\n\
Greatest Decrease in Profits: {min_monthly_change_date} (${min_monthly_change}) '''

#print financial analysis
print(financial_analysis)

#export financial analysis to PyBank.txt file
file = open("PyBank.txt", "w")
file.writelines(financial_analysis)
file.close()