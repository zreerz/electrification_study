import csv 
from os import listdir
from os.path import isfile, join
import numpy as np
import matplotlib.pyplot as plt

paneldump_path='paneldump/'
volt_val = 1000/110 # kW/V to A conversion fraction
curr_val = 0 # current value 
c_list = [] # list of current values
f_list = []
onlyfiles = [f for f in listdir(paneldump_path) if isfile(join(paneldump_path, f)) and f.startswith( "paneldump" )]
def paneldumpparse(f_name) : 
	curr_list = []
	house_curr = {}
	house_dict = {} # {house_# : { time : power }}
	with open(paneldump_path+f_name, newline='') as csvfile : 
		fr = csv.reader(csvfile, delimiter=',', quotechar='|')
		next(fr)
		for row in fr :
			curr_val = float(row[3])*volt_val
			if not house_dict : # first line of dictionary
				house_dict[row[1]] = {row[0]:curr_val}
			else : 
				if row[1] in house_dict : # check if house is in list 
					if row[0] in house_dict[row[1]].keys() : # check if timestamp is in the list
						house_dict[row[1]][row[0]] = float(house_dict[row[1]][row[0]])+curr_val
						# if '2018-01-15 02:00:00 PST' in row[0] and 'house_99_ELEC' in row[1]:
							# print(row[0],row[1],float(house_dict[row[1]][row[0]]))
					else : #add new house key
						house_dict[row[1]][row[0]]=curr_val
				else : #timestamp not in list
					house_dict[row[1]]={row[0]:curr_val}
					# if '2018-01-15 02:00:00 PST' in row[0] and 'house_99_ELEC' in row[1]:
						# print(curr_val)
						# print(row[0],row[1],float(house_dict[row[1]][row[0]]))
	for house in house_dict : 
		# print(house_dict)
		total_energy = max(float(d) for d in house_dict[house].values())
		max_curr = (max(float(d) for d in house_dict[house].values())) 
		curr_list.append(max_curr)
		house_curr[house]=max_curr
	print()
	return curr_list 



# Variables for plotting
y_plt = []
x_label = ['50', '100', '150', '200', '200+']
x_plt = np.arange(len(x_label))
x_shift = np.NaN
for file_name in onlyfiles : 
	c_list = []
	panel_50 = 0
	panel_100 = 0
	panel_150 = 0
	panel_200 = 0
	panel_large = 0
	c_list = (paneldumpparse(file_name))
	for val in c_list : 
		if val < 40 : 
			panel_50 = panel_50+1; 
		elif val >= 40 and val < 80 : 
			panel_100 = panel_100+1;
		elif val >= 80 and val < 120 :
			panel_150 = panel_150+1; 
		elif val >= 120 and val < 160 :
			panel_200 = panel_200+1; 
		else : 
			panel_large = panel_large+1;
	y_plt = [panel_50, panel_100, panel_150, panel_200, panel_large]
	# print(c_list)
	print(file_name[10:],y_plt)
	plt.bar(x_plt, y_plt, align='center', label=file_name[10:])
plt.xticks(x_plt, x_label)
plt.ylabel('Number of Houses')
plt.xlabel('Electrical Panel Size (A)')
plt.legend()
plt.tight_layout()
# plt.show()


	# f_list.append(file_name)

	# plt.hist(paneldumpparse(file_name), bins=2, alpha=0.5, label=file_name)


# plt.legend(loc='upper right')
# plt.show()


