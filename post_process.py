import csv 
from os import listdir
from os.path import isfile, join

paneldump_path='paneldump/'
volt_val = 1000/220
curr_val = 0
onlyfiles = [f for f in listdir(paneldump_path) if isfile(join(paneldump_path, f)) and f.startswith( "paneldump" )]

house_dict = {}
with open(paneldump_path+'/'+onlyfiles[0], newline='') as csvfile : 
	print(onlyfiles[0])
	fr = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(fr)
	for row in fr :
		curr_val = float(row[3])*volt_val
		if not house_dict : # first line of dictionary
			house_dict[row[0]] = {row[1]:curr_val}
		else : 
			if row[0] in house_dict : # check if timestamp in list 
				if row[1] in house_dict[row[0]].keys() :
					house_dict[row[0]][row[1]] = float(house_dict[row[0]][row[1]])+curr_val
				else : #add new house key
					house_dict[row[0]][row[1]]=curr_val
			else : #timestamp not in list
				house_dict[row[0]]={row[1]:curr_val}

print(house_dict)

