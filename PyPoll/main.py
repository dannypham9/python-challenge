#import to read files
import os
import csv

#create list variables
votes=[]
candidates= []
candidatelist=[]

Correy=[]
Li=[]
OTooley=[]
Khan=[]

#create path
csvpath= os.path.join("resources", "PyPoll_Resources_election_data.csv")

#open csv file
with open(csvpath) as csvfile:
	csvreader= csv.reader(csvfile, delimiter=",")
	header=next(csvreader)

#assign columns
	for i in csvreader:
		votes.append(i)
		candidates.append(i[2])
	
	#find total votes
		totalvotes= len(votes)
	print(totalvotes)
	
	#find all the unique candidates
	candidatelist= list(set(candidates))
	print(candidatelist)

	#count total votes for each candidate
	for j in candidates:
		if j== "Correy":
			Correy.append(candidates)
			correyvotes= len(Correy)
		elif j== "Li":
			Li.append(candidates)
			livotes=len(Li)
		elif j== "Khan":
			Khan.append(candidates)
			khanvotes=len(Khan)
		else: 
			OTooley.append(candidates)
			otooleyvotes=len(OTooley)	
	print(correyvotes)
	print(livotes)
	print(khanvotes)
	print(otooleyvotes)

	#find percentage of votes for each candidate
	percentcorrey= "{:.0%}".format(correyvotes/totalvotes)
	percentli= "{:.0%}".format(livotes/totalvotes)
	percentkhan= "{:.0%}".format(khanvotes/totalvotes)
	percentotooley= "{:.0%}".format(otooleyvotes/totalvotes)
	
	print(percentcorrey)
	print(percentli)
	print(percentkhan)
	print(percentotooley)
	
	#determine winner by checking which percentage was the highest
	if percentkhan > max(percentotooley, percentli, percentcorrey):
		Winner= "Khan"
	elif percentcorrey > max(percentkhan,percentli, percentotooley):
		Winner= "Correy"
	elif percentli > max(percentkhan, percentotooley, percentcorrey):
		Winner= "Li"
	elif percentotooley > max(percentkhan, percentli, percentcorrey): 
		Winner= "O'Tooley"

#create output path
output_path= os.path.join("Analysis", "analysis.txt")

#open text file
with open(output_path, 'w', newline='') as textfile:
	csvwriter= csv.writer(textfile)
	csvwriter.writerow(['Election Results'])
	csvwriter.writerow(['-----------------'])

	csvwriter.writerow([f'Total votes: {totalvotes}'])
	csvwriter.writerow(['-----------------'])

	csvwriter.writerow([f'Khan: {percentkhan} ({khanvotes})'])
	csvwriter.writerow([f'Correy: {percentcorrey} ({correyvotes})'])
	csvwriter.writerow([f'Li: {percentli} ({livotes})'])
	csvwriter.writerow([f'O\'Tooley: {percentotooley} ({otooleyvotes})'])
	csvwriter.writerow(['-----------------'])

	csvwriter.writerow([f'Winner: {Winner}'])