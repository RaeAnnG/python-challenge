# import the os module
import os

# import Module for reading CSV files
import csv

# import Pandas
import pandas as pd

# read file
budget_data_file = os.path.join('Resources', 'budget_data.csv')

# reading Method using CSV module
Total = 0
Months = 0

NetchangeList =[] 
PreviousChange = 0
MaxIncrease = 0
MaxDecrease = 0
MaxIncreaseDate = ""
MaxDecreaseDate = ""

#assign Title and line break
title = (f"Financial Analysis\n")
line = (f"---------------------\n")

#print Header Financial Analysis
print(title)

#print line break
print (str(line))

with open(budget_data_file) as csvfile:

    # specify delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    first_row = next(csvreader)

    #set starting points and change points
    Months = Months + 1
    Total = Total + int(first_row[1])
    PreviousChange = int(first_row[1])
    # For loop for calculations
    for row in csvreader:
        if Months > 0:
            Months = Months + 1
            Total += int(row[1])
            Netchange = int(row[1])- PreviousChange
            PreviousChange = int(row[1])
            NetchangeList.append(Netchange)
            if Netchange > MaxIncrease:
                MaxIncrease = Netchange
                MaxIncreaseDate = row[0]
        #PreviousChange
            if Netchange < MaxDecrease:
                MaxDecrease = Netchange
                MaxDecreaseDate = row[0]

    Averagechange = sum(NetchangeList)/len(NetchangeList)    

#Print Results
print("Total Months: " + str(Months))
print("Total: " + "$" + str(Total))
print("Average Change: " + "$" + str(Averagechange))
print("Greatest Increase in Profits: " + str(MaxIncreaseDate) + " ($" + str(MaxIncrease) + ")")
print("Greatest Decrease in Profits: " + str(MaxDecreaseDate) + " ($" + str(MaxDecrease) + ")")

#output file
pybank_txt = os.path.join('Resources','pybank.txt')
# Open the file using "write" mode. Specify the variable to hold the contents
with open(pybank_txt, "w") as pbtextfile:

    #assign Title and line break
    title = (f"Financial Analysis\n")
    line = (f"---------------------\n")
    
    #print Header Financial Analysis
    pbtextfile.write(str(title))

    #print line break
    pbtextfile.write(str(line))
    
    PyBankMonths = (
    f"\n\nTotal Months: {Months}\n")


    PyBankTotal = ("Total: " + '$' + str(Total))

    print (str(line))   
    
    PBAveragechange = (
    f"\n\nAverage Change: {Averagechange}\n"
    f"--------------------")

    PBGreatestIncrease = (
    f"\nGreatest Increase: {MaxIncrease}\n"
    f"--------------------")

    PBGreatestDecrease = (
    f"\nGreatest Increase: {MaxDecrease}\n"
    f"--------------------")   

    #Print it to the file
    pbtextfile.write(PyBankMonths)
    pbtextfile.write(PyBankTotal)
    pbtextfile.write(PBAveragechange)
    pbtextfile.write(PBGreatestDecrease)
    pbtextfile.write(PBGreatestDecrease)

    for PyBankSummery in PyBankTotal:
        if Months > 0:
            Months = Months + 1
            Total += int(row[1])
            Netchange = int(row[1])- PreviousChange
            PreviousChange = int(row[1])
            NetchangeList.append(Netchange)
            if Netchange > MaxIncrease:
                MaxIncrease = Netchange
                MaxIncreaseDate = row[0]
        #PreviousChange
            if Netchange < MaxDecrease:
                MaxDecrease = Netchange
                MaxDecreaseDate = row[0]

    Averagechange = sum(NetchangeList)/len(NetchangeList)  
    
    #print line break
    print("---------------------")


      