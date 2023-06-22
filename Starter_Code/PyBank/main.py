# import modules
import os
import csv

csvpath = os.path.join('..','PyBank', 'Resources', 'budget_data.csv')

output = os.path.join('..', 'PyBank', 'Analysis', 'analysis.txt')


monthCounter = 0
profitLoss = 0

#initialize change variables
profits = []
monthlyChanges = []
dates = []
initialProfit = 1088983
lastProfit = 0
totalChanges = 0
averageChange = 0
maxChange = 0
minChange = 0
increaseDate = 0
decreaseDate = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    header = next(csvreader)
    for row in csvreader:
        monthCounter = monthCounter + 1
        profitLoss = profitLoss + int(row[1])

        dates.append(row[0])

        #Calculate the change from the previous month
        lastProfit = int(row[1])
        monthlyChange = lastProfit - initialProfit

        #Add change to list of Monthly Changes
        monthlyChanges.append(monthlyChange)

        totalChanges = totalChanges + monthlyChange

        #Set initialProfit to this month to be used in the next iteration
        initialProfit = lastProfit


    maxChange = max(monthlyChanges)
    minChange = min(monthlyChanges)
    averageChange = (totalChanges/(monthCounter-1))

    #determine the dates for the greatest increase and decrease
    increaseDate = dates[monthlyChanges.index(maxChange)]
    decreaseDate = dates[monthlyChanges.index(minChange)]


with open('analysis.txt', "w") as text:
    text.write("Financial Analysis \n")
    text.write("----------------------------\n")
    text.write("Total Months: " + str(monthCounter) + "\n")
    text.write("Total: $" + str(profitLoss) + "\n")
    text.write("Average Change: $" + str(averageChange) + "\n")
    text.write("Greatest Increase in Profits: " + str(increaseDate) + "($" + str(maxChange) + ")\n")
    text.write("Greatest Decrease in Profits: " + str(decreaseDate) + "($" + str(minChange) + ")\n")

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(monthCounter))
print("Total: $" + str(profitLoss))
print("Average Change: $" + str(averageChange))
print("Greatest Increase in Profits: " + str(increaseDate) + "($" + str(maxChange) + ")")
print("Greatest Decrease in Profits: " + str(decreaseDate) + "($" + str(minChange) + ")")