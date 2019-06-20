import csv

csvpath = "budget_data.csv"

#def financial_analysis(data_group):

print("Financial Analysis")
print("---------------------------")
  
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    # print(f"Name:{csv_header}")
    total = 0
    data = []
    average_change = 0
    total_change = 0
    max_change = 0
    min_change = 0
    for row in csvreader:

        #variables used to hold the parameters of the file
        month = row[0]
        profit_loss = float(row[1])
        
        #calculates the total profit/losses for the entire period
        total = total + float(row[1])       

        # add the values to the data list
        data.append([month,profit_loss])

    for i in range(len(data)-1):
       
        data_row = data[i]
        current_month = data_row[1]
        next_row = data[i+1]
        next_month = next_row[1]
       
        #calculates the change per month
        change = next_month - current_month
        total_change = total_change + change
        if change > 0 and change > max_change:
            max_change = change
            date_max = data_row[0]
        if change < 0 and change < min_change:
            min_change = change
            date_min = data_row[0]
                 
    average_change = total_change/(len(data)-1)

    print (f"Total number of months:{len(data)}")
    print(f"Total amount for the entire period: {total}")
    print(f"Average Change: {average_change}")
    print(f"Greatest Increase in Profits: {date_max} ({max_change})") 
    print(f"Greatest Decrease in Profits: {date_min} ({min_change})")

text_file = open("pybankoutput.txt","w")

text_file.write(f"Financial Analysis \n --------------------------- \nTotal number of months:{len(data)}\n Total amount for the entire period: {total}\nAverage Change: {average_change}\nGreatest Increase in Profits: {date_max} ({max_change})\nGreatest Decrease in Profits: {date_min} ({min_change}) ")
