import csv

csvpath = "election_data.csv"

print("Election Results")
print("---------------------------")

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    # print(f"Name:{csv_header}")
    
    data = []
    Khan_total = 0
    Correy_total = 0
    Li_total = 0
    Tooley_total = 0
    

    # calculates the percentage of each candidate, accepts partial and total votes for parameters and 
    #returns the percentage
    def percent_vote(partial_vote,total_vote):

        percentage = partial_vote/total_vote * 100

        return f'{percentage:.3g}'
               
    for row in csvreader:

        #variables used to hold the parameters of the file
        Voter_ID = row[0]
        county = row[1]
        candidate = row[2]    

        # counts the votes of each candidate
        if candidate == "Khan":
            Khan_total = Khan_total + 1                      
        elif candidate == "Correy":
            Correy_total = Correy_total + 1
        elif candidate == "Li":
            Li_total = Li_total + 1
        elif candidate == "O'Tooley":
            Tooley_total = Tooley_total + 1

        # adds the values to the data list
        data.append([Voter_ID,county,candidate])

    # creates the list of candidates' final votes
    tally = [("Khan",Khan_total),("Correy",Correy_total), ("Li",Li_total),("O'Tooley",Tooley_total)]

    # sorts the winner in the tally 
    votes = lambda person:person[1]
    tally.sort(key=votes, reverse=True)
    for_the_win = tally[0]
    
    #prints the total and each candidate's results
    
    print (f'Total number of voters: {len(data)}')
    
    print(f'Khan: {percent_vote(Khan_total,len(data))}% ({Khan_total})')
    print(f'Correy: {percent_vote(Correy_total,len(data))}% ({Correy_total})')
    print(f'Li: {percent_vote(Li_total,len(data))}% ({Li_total})')
    print(f"O'Tooley: {percent_vote(Tooley_total,len(data))}% ({Tooley_total})")

    print("---------------------------")
    print(f'Winner:  {for_the_win[0]}')
    print("---------------------------")

text_file = open("PyPolloutput.txt","w")

text_file.write(f"---------------------------\n Election Results\n ---------------------------\n Total number of voters: {len(data)} \n Khan: {percent_vote(Khan_total,len(data))}% ({Khan_total})\nCorrey: {percent_vote(Correy_total,len(data))}% ({Correy_total})\nLi: {percent_vote(Li_total,len(data))}% ({Li_total})\nO'Tooley: {percent_vote(Tooley_total,len(data))}% ({Tooley_total})\n---------------------------\nWinner:  {for_the_win[0]}\n---------------------------")
