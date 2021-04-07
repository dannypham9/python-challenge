#import to read files and to create file paths
import csv
import os

output=['totalmonths', 'totalprofloss', 'monthly_average', 'bestmonth', 'worstmonth']

#create path for file
csvpath= os.path.join("Resources", "budget_data.csv")

#opening the csv file
with open(csvpath) as csvfile:
	#set variables
	dates=[]
	profit_loss=[]
	monthly_changes=[]
	month=[]

	#separated by comma
	csvreader= csv.reader(csvfile, delimiter=',')
	
	#reading header row
	csvheader= next(csvreader)
	
	#Assign columns
	for row in csvreader:
		dates.append(row[0])
		profit_loss.append(int(row[1]))
	
	#count the amount of months
	totalmonths=len(dates)
	print(totalmonths)

	#sum of the profit/loss for the period
	totalprofloss= sum(profit_loss)
	print(totalprofloss)

	#find average monthly change
	for initial_month in range(len(profit_loss)-1):
		change= profit_loss[initial_month+1]- profit_loss[initial_month]
		monthly_changes.append(change)
	totalchange= sum(monthly_changes)
	monthly_average= round(totalchange/len(monthly_changes), 2)
	print(monthly_average)

	#find greatest increase
	greatest_increase= max(monthly_changes)
	print(greatest_increase)
	#find the month the change occured
	i = monthly_changes.index(greatest_increase)
	bestmonth= dates[i+1]
	print(bestmonth) 

	#find greatest decrease
	greatest_decrease=min(monthly_changes)
	print(greatest_decrease)
	#find the month the change occurred
	j = monthly_changes.index(greatest_decrease)
	worstmonth= dates[j+1]
	print(worstmonth)

#find file to write to for analysis
output_path= os.path.join("Analysis", "analysis.txt")

#open file
with open(output_path, 'w', newline='') as textfile:
	csvwriter= csv.writer(textfile)
	csvwriter.writerow(['Finacial Analysis'])
	csvwriter.writerow(['-----------------'])

	csvwriter.writerow(['Total months:' + str(totalmonths)])
	csvwriter.writerow([f'Total: ${totalprofloss}'])
	csvwriter.writerow([f'Average Change: ${monthly_average}'])
	csvwriter.writerow([f'Greatest Increase in Profits: {bestmonth} (${greatest_increase})'])
	csvwriter.writerow([f'Greatest Decrease in Profits: {worstmonth} (${greatest_decrease})'])