import os
import csv

votes=[]

csvpath= os.path.join("resources", "PyPoll_Resources_election_data.csv")

with open(csvpath) as csvfile:
	csvreader= csv.reader(csvfile, delimiter=",")
	header=next(csvreader)

	for i in csvreader:
		votes.append(i)
	print(len(votes))
		