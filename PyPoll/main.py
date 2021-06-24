import os
import csv

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as election_data:
    
    data = csv.reader(election_data, delimiter=',') # CONVERTS DATA TO CSV
    election_header = next(data)

    election_list = [row for row in data]
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0
    vote_count = 0
    votes_uncounted = 0
     
    for y in election_list:
       if y[2] == "Khan": 
           Khan_count += 1 # COUNTS VOTES FOR KHAN
           vote_count += 1 # COUNTS TOTAL VOTES
       elif y[2] == "Correy":
            Correy_count += 1 # COUNTS VOTES FOR CORREY
            vote_count += 1 # COUNTS TOTAL VOTES
       elif y[2] == "Li":
            Li_count += 1 # COUNTS VOTES FOR LI
            vote_count += 1 # COUNTS TOTAL VOTES
       elif y[2] == "O'Tooley":
            OTooley_count += 1 # COUNTS VOTES FOR O'TOOLEY
            vote_count += 1 # COUNTS TOTAL VOTES
       else:
           votes_uncounted += 1
           print("Alert! " + str(votes_uncounted) + " Uncounted Votes") # CHECKS FOR UNCOUNTED VOTES

    Khan_percent = '{0:,.1f}'.format(Khan_count/vote_count*100)
    Correy_percent = '{0:,.1f}'.format(Correy_count/vote_count*100)
    Li_percent = '{0:,.1f}'.format(Li_count/vote_count*100)
    OTooley_percent = '{0:,.1f}'.format(OTooley_count/vote_count*100)

    print("  ")
    print("  ")
    print("ELECTION RESULTS")
    print("------------------------------")
    print("Total Votes: " + '{0:,}'.format(vote_count)) # PRINTS TOTAL NUMBER OF VOTES CAST
    print("------------------------------")
    print("Khan: " + '{0:,}'.format(Khan_count) + " votes / " + str(Khan_percent) + "%") #KHAN TOTAL + %
    print("Correy: " + '{0:,}'.format(Correy_count) + " votes / " + str(Correy_percent) + "%") #CORREY TOTAL + %
    print("Li: " + '{0:,}'.format(Li_count) + " votes / " + str(Li_percent) + "%") #LI TOTAL + %
    print("O'Tooley: "  + '{0:,}'.format(OTooley_count) + " votes / " + str(OTooley_percent) + "%") #OTOOLEY TOTAL + %
    print("------------------------------")

    Winner_Name = ["Khan","Correy","Li","O'Tooley",]
    Winner_Count = [Khan_count,Correy_count,Li_count,OTooley_count,votes_uncounted]
    Winner_Dict = dict(zip(Winner_Name,Winner_Count)) #CREATE A DICTIONARY BY ZIPPING TWO LISTS

    Winner = max(Winner_Dict, key=lambda key: Winner_Dict[key]) #USE STACKOVERFLOW TO FIND KEY WITH MAX VALUE 
    print(f'Winner: {Winner}')
    print("------------------------------")
    print("  ")
    print("  ")

txtpath = os.path.join("Analysis", "main_pypoll.txt")
with open(txtpath,"w") as text_file: 
    text_file.write("ELECTION RESULTS\n")
    text_file.write("------------------------------\n")
    text_file.write("Total Votes: " + '{0:,}'.format(vote_count) + "\n")
    text_file.write("------------------------------\n")
    text_file.write("Khan: " + '{0:,}'.format(Khan_count) + " votes / " + str(Khan_percent) + "%\n")
    text_file.write("Correy: " + '{0:,}'.format(Correy_count) + " votes / " + str(Correy_percent) + "%\n")
    text_file.write("Li: " + '{0:,}'.format(Li_count) + " votes / " + str(Li_percent) + "%\n")
    text_file.write("O'Tooley: "  + '{0:,}'.format(OTooley_count) + " votes / " + str(OTooley_percent) + "%\n")
    text_file.write("------------------------------\n")
    text_file.write(f'Winner: {Winner}\n')
    text_file.write("------------------------------\n")


#BOOYOW

#BIG THANKS TO:
#  LUIS (TUTOR) FOR GETTING ME STARTED WITH LOOP BASICS
#  SONY (CLASSMATE) FOR THE FORMAT FORMULA
#  THOMAS (CLASSMATE) FOR THE EXPORT HELP
#  ERIKA (PARTNER) FOR GRANTING ME TIME TO WORK