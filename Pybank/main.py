import csv
import os
import string


TotalMonths = 0
Total = 0.00
Monthlychange = 0
PreviousMonth=0
CurrentMonth=0
Month_Increase=0
Month_Decrease=0
GreatestDecrease=0
GreatestIncrease=0
average_Change =0




budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csv_file:
    csvreader = csv.reader(csv_file)
    csv_reader = next(csvreader)
    # add a next() to initialize first row parameters previousmonth and current month 
    counter=5

    data=[]
    for row in csvreader:
        data.append(row[0])
        Total += float(row[1])

        CurrentMonth=int(row[1])
        
        if PreviousMonth != 0:
           
            Monthlychange += PreviousMonth-CurrentMonth
    
        PreviousMonth=int(row[1])
        if int(row[1])>int(GreatestIncrease):
            GreatestIncrease=row[1]
            Month_increase=row[0]

    

        if int(row[1])<int(GreatestDecrease):
            GreatestDecrease=row[1]
            Month_Decrease=row[0]

            
sum_months = len(data)

average_change = Monthlychange / int(sum_months) * -1 
   

#print out in terminal
print("Financial Analysis")
print("------------------------------")
print(f"Total months: " +str(sum_months))
print(f"Total: $" + str(Total))
print(f"Average Change: $" + str(average_change))
print(f"Greates increase in Profits: " + Month_increase + " " + str(GreatestIncrease))
print(f"Greates decrease in Profits: " + Month_Decrease + " " + str(GreatestDecrease))

#write to file
with open("PyBankanalysis.txt", "w") as analysis:
    analysis.write("Financial Analysis\n")
    analysis.write("------------------------------\n")
    analysis.write(f"Total months: " +str((sum_months))+"\n")
    analysis.write(f"Total: $" + str(Total)+"\n")
    analysis.write(f"Average Change: $" + str(average_change)+"\n")
    analysis.write(f"Greates increase in Profits: " + Month_increase + " " + str(GreatestIncrease)+"\n")
    analysis.write(f"Greates decrease in Profits: " + Month_Decrease + " " + str(GreatestDecrease)+"\n")

 

    
