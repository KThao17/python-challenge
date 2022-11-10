import os
import csv

budget_csv = 'Starter_Code\Instructions/PyBank\Resources/budget_data.csv' 

total_months = 0
net_total = 0
profit_losses = []
average_changes = []
pl_change = []
Date = []

with open(budget_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
    
       total_months = total_months + 1
       net_total = net_total + int(row[1])
       profit_losses.append(row[1])
       Date.append(row[0]) 
       print(profit_losses)
       print(Date)

    for x in range(1,len(profit_losses)):
        pl_change.append(int(profit_losses[x])-int(profit_losses[x-1]))

    f = open("financial_analysis.txt", "w")
    print("Financial Analysis")
    print("----------------------------------------------")
    print("Total Months: " + str(total_months))
    total_average_change = sum(pl_change) / len(pl_change)
    print(f'Average Change:${total_average_change:.2f}') 
    plgreatestincrease = max(pl_change)
    plgreatestdecrease = min(pl_change)
    plgreatestincrease_date = Date[pl_change.index(plgreatestincrease)+1]
    plgreatestdecrease_date = Date[pl_change.index(plgreatestdecrease)+1]
    print(f'Greatest Increase in Profits: {plgreatestincrease_date} (${plgreatestincrease})')
    print(f'Greatest Decrease in Profits: {plgreatestdecrease_date} (${plgreatestdecrease})') 
        
        