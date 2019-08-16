import csv 
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

paneldump_path='paneldump/'
volt_val = 1000/220
curr_val = 0
c_list = []
f_list = []
onlyfiles = [f for f in listdir(paneldump_path) if isfile(join(paneldump_path, f)) and f.startswith( "paneldump" )]
# HISTOGRAM PLOTS
plt.xlabel('Panel Size')
plt.ylabel('Number of Houses')
def paneldumpparse(f_name) : 
	with open(paneldump_path+'/'+f_name, newline='') as csvfile : 
		curr_list = []
		house_curr = {}
		house_dict = {}
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
		# if max_curr < 80 : 
		curr_list.append(round(max_curr))
		# 	curr_list.append(80)
		# elif max_curr>=80 and max_curr<160 : 
		# 	curr_list.append(160)
		# else : 
		# 	curr_list.append(320) 
		house_curr[house]=max_curr
	return curr_list 

for file_name in onlyfiles : 
	# c_list = []
	c_list.append(paneldumpparse(file_name))
	print(c_list)
	print(file_name)
	f_list.append(file_name)

plt.hist(c_list, bins=2, alpha=0.5, label=f_list)

plt.legend(loc='upper right')
plt.show()


