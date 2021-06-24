# python-challenge
UNC BOOTCAMP Python HW

Re: PyPoll

ACCESSING THE  DATA:

    a. define an import path to the csv file
    b. access the file
    c. convert the object into a readible list
    d. eliminate the header row

--------------------------------------------
ESTABLISH VARIABLES AND EMPTY LISTS:

    a. 0-start variable to track each candidate appearance in list
    b. 0-start variable to track all votes in list
    c. A method to ensure I have counted all candidate votes

Given lack of skill with dictionaries, I needed another way to ensure I had counted all candidates. After scrolling through the printed list for names,I created "votes_uncounted" to track whether I had missed a candidate who recieved votes but did not appeared in the "election_list".

--------------------------------------------
RUN CONDITONAL FOR LOOPS:

    a. count votes for each candidate by looping through election_list
    b. count total votes for looping through election_list
    c. append canddiate vote count to their own list
    d. append total vote count to a list
    e. append unaccounted votes to a list and send alert

--------------------------------------------
CALCULATE VOTE PERCENTAGE AND FORMAT RESULT:

    a. divide each candidate count by total votes to caculate percentage
    b. format as percent with 1 decimal
    c. calculate winner

--------------------------------------------
CALCULATE WINNER:

    a. create list with candidate names 
    b. create list with candidate counts
    c. zip two list into dictionary, mindful of key:value order
    d. research how to extract max value from dictionary and return key

--------------------------------------------
PRINT RESULTS TO TERMINAL:

    a. print caculations using variables and list methods
    b. format to include commas and descriptive language
    c. mind space and syntax

--------------------------------------------
PRINT RESULTS TO TXT:

    a. define export path and name txt file
    b. open txt file with over-write permission
    c. write each line of caculations to txt file + new line tag

--------------------------------------------    
CELEBRATE & GIVE THANKS //

#  BOOYOW
#  LUIS (TUTOR) FOR GETTING ME STARTED WITH LOOP BASICS
#  SONY (CLASSMATE) FOR THE FORMAT FORMULA
#  THOMAS (CLASSMATE) FOR THE EXPORT HELP
#  STACKOVERLOW CONTRIBUTOR (RESOURCE) FOR DICTIONARY LOC
#  ERIKA (PARTNER) FOR GRANTING ME TIME TO WORK



Re: PyBank

ACCESSING THE  DATA:

    a. define an import path to the csv file
    b. access the file
    c. convert the object into a readible list
    d. eliminate the header row

--------------------------------------------
ESTABLISH VARIABLES & EMPTY LISTS:

    a. 0-start variable to count number of rows in data
    b. create a list with complete copy of data set
    c. create a list to store money values 
    d. create a list to store date values 

--------------------------------------------
PRINT HEADER  & CALCULATE TOTALS:

    a. print analysis header
    b. calculate the length of money_lst and print result with text
    c. convert numerical strings in money_lst into integers as money_num
    d. calculate the sum of money_num and print result with text

--------------------------------------------
CACULATE CHANGE:

    a. create a list to store difference in money_num entry to entry
    b. for loop money_num starting at 1 for the length of the list
    c. append the difference from one entry to the next into money_change
    d. check money_change values and length
    e. calculate average change with mean method from statistics library
    f. print results

--------------------------------------------
CALCULATE INCREASE, DECREASE, & ASSOCIATED DATES:

    a. use max method money_change list to find highest integer
    b. print result
    c. create variable to hold max_increase_date calculation
    d. *take a breath*
    e. match value in date_lst w/ index the money_change for max value
    f. add 1 to index to match list lengths
    h. use min method step for step in steps(a,f)
    i. print results

--------------------------------------------
PRINT RESULTS TO TXT:

    a. define export path and name txt file
    b. open txt file with over-write permission
    c. write each line of caculations to txt file + new line tag

--------------------------------------------    
CELEBRATE & GIVE THANKS //

#  BOOM
#  SEAN (TEACHER) FOR HELP WITH THE DATES
#  MUHAMMED (ASKBCS) FOR HELP WITH THE AVERAGE
#  FELIPE (TA) FOR HELP WITH LIST SIZE ERROR
#  ANITA (CLASSMATE) FOR THE LOOP CONCEPT
#  HEIR (SON) FOR THAT ENCOURAGING SMILE