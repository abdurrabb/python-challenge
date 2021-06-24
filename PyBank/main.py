import os
import csv
from statistics import mean

csvpath = os.path.join('Resources','budget_data.csv') #SETS PATH TO DATA

with open(csvpath,'r') as pybank_data: #OPENS FILE AS OBJECT

    budget_csv = csv.reader(pybank_data, delimiter=",") # CONVERTS PY_BANK INTO READABLE LIST
    budget_header = next(budget_csv)
    # for row in budget_csv: 
    #     print(row)

    row_count = 0
    data = [row for row in budget_csv]
    money_lst = [row[1] for row in data] #SUCCESS
    date_lst =[row[0] for row in data] #SUCCESS
    
    print("  ")
    print("------------------------------")
    print("FINANCIAL ANALYSIS")
    print("------------------------------")
    
    print(f'TOTAL MONTHS: {len(money_lst)}') #THE TOTAL NUMBER OF MONTHS IN DATASET

    money_num = [int(i) for i in money_lst] #CONVERTS STRING TO INTEGER VALUES FOR MATHING
    
    total_amount = sum(money_num) #CALCULATES NET TOTAL PROFIT/LOSS
    print(f'NET PROFIT/LOSS: $''{0:,}'.format(total_amount))

    money_change = []
    for amount in range(1,len(money_num)):
        money_change.append(money_num[amount] - money_num[amount-1]) #CREATES LIST OF CHANGES

    # print(money_change) #SUCCESS
    # print(sum(money_change)) #FAIL
    # print(len(money_change)) #SUCCESS

    ave_change = mean(money_change)
    print(f'AVERAGE CHANGE IN PROFIT/LOSS: $' '{0:,.2f}'.format(ave_change))

    max_increase = max(money_change) #CALCULATES GREATEST INCREASE IN PROFITS
    max_increase_date = date_lst[money_change.index(max_increase) + 1]
    
    print(f'GREATEST INCREASE IN PROFIT/LOSS: $' + '{0:,}'.format(max_increase))
    print("GREATEST INCREASE DATE: " + (max_increase_date))
   
    max_decrease = min(money_change) #CALCULATES GREATEST DECREASE IN PROFITS
    max_decrease_date = date_lst[money_change.index(max_decrease) + 1]
    print(f'GREATEST DECREASE IN PROFIT/LOSS: $' '{0:,}'.format(max_decrease))
    print("GREATEST DECREASE DATE: " + (max_decrease_date))
    print("------------------------------")

    txtpath = os.path.join("Analysis", "main_pybank.txt") #PREPARES TXT FILE
with open(txtpath,"w") as text_file: 
    text_file.write("FINANCIAL ANALYSIS\n") #WRITES TO TXT FILE
    text_file.write("------------------------------\n")
    text_file.write(f'TOTAL MONTHS: {len(money_lst)}\n')
    text_file.write("NET PROFIT/LOSS: $" + '{0:,}'.format(total_amount) + ' \n')
    text_file.write("------------------------------\n")
    text_file.write("AVERAGE CHANGE IN PROFIT/LOSS: $" + '{0:,.2f}'.format(ave_change) + ' \n')
    text_file.write("------------------------------\n")
    text_file.write(f'GREATEST INCREASE IN PROFIT/LOSS: $' '{0:,}'.format(max_increase)+ ' \n')
    text_file.write(f'GREATEST INCREASE DATE: {max_increase_date} \n')
    text_file.write("------------------------------\n")
    text_file.write(f'GREATEST DECREASE IN PROFIT/LOSS: $' '{0:,}'.format(max_decrease)+ ' \n')
    text_file.write(f'GREATEST DECREASE DATE: {max_decrease_date} \n')
    text_file.write("------------------------------\n")

    #BOOM

#BIG THANKS TO:
#  FELIPE (TA) FOR CLEAN LIST SIZE FIX
#  ANITA (CLASSMATE) FOR THE LOOP CONCEPT
#  HEIR (SON) FOR THAT ENCOURAGING SMILE