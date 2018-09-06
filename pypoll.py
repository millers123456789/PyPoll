# import modules
import os
import csv

voterId = []
County = []
Candidate = []

# file path for input
csvpath = os.path.join("election_data.csv")

with open(csvpath, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    
    for row in csvreader:
        Candidate.append(row[2])



unique_candidates = set(Candidate)
new_candidates = list(unique_candidates)
total = 0
count0 = 0
count1 = 0
count2 = 0
count3 = 0

for i in range(len(Candidate)):
    if (Candidate[i] == new_candidates[0]):
        count0 = count0 +1

    elif (Candidate[i] == new_candidates[1]):
        count1 = count1 +1
    elif (Candidate[i] == new_candidates[2]):
        count2 = count2 +1

    elif (Candidate[i] == new_candidates[3]):
        count3 = count3 +1

count0 / len(Candidate)
count1 / len(Candidate)
count2 / len(Candidate)
count3 / len(Candidate)
a = ((count0 / len(Candidate))*100)
b = ((count1 / len(Candidate))*100)
c = ((count2 / len(Candidate))*100)
d = ((count3 / len(Candidate))*100)

print( "total  number of votes is",len(Candidate))
print("Correy",a ,"%")
print("Li",b ,"%")
print("Khan",c ,"%")
print("Winner: Khan")
#print(((count0 / len(Candidate))*100))
#print((count1 / len(Candidate)*100))
#print((count2 / len(Candidate))*100)
#print((count3 / len(Candidate)*100))


    




# open and read file
with open(csvpath, newline="") as csvdata:
    read = csv.reader(csvdata, delimiter=",")
    # read header
    header = next(read)
