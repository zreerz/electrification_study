import csv 
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

paneldump_path='paneldump/'
volt_val = 1000/220
curr_val = 0
house_curr = {}
curr_list = []
c_list = []
onlyfiles = [f for f in listdir(paneldump_path) if isfile(join(paneldump_path, f)) and f.startswith( "paneldump" )]
house_dict = {}
# HISTOGRAM PLOTS
plt.xlabel('Panel Size')
plt.ylabel('Number of Houses')
def paneldumpparse(f_name) : 
	with open(paneldump_path+'/'+f_name, newline='') as csvfile : 
		fr = csv.reader(csvfile, delimiter=',', quotechar='|')
		next(fr)
		for row in fr :
			curr_val = float(row[3])*volt_val
			if not house_dict : # first line of dictionary
				house_dict[row[1]] = {row[0]:curr_val}
			else : 
				if row[1] in house_dict : # check if timestamp in list 
					if row[0] in house_dict[row[1]].keys() :
						house_dict[row[1]][row[0]] = float(house_dict[row[1]][row[0]])+curr_val
					else : #add new house key
						house_dict[row[1]][row[0]]=curr_val
				else : #timestamp not in list
					house_dict[row[1]]={row[0]:curr_val}

	for house in house_dict : 
		max_curr = (max(float(d) for d in house_dict[house].values()))
		curr_list.append(max_curr)
		house_curr[house]=max_curr
	return curr_list 

for file_name in onlyfiles : 
	print(file_name)
	c_list.append(paneldumpparse(file_name))

# print(c_list)

plt.hist(c_list,bins=3)


plt.show()


