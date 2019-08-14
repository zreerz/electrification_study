import csv 
import gridlabd
import os
import glob
from shutil import copyfile

gas_heat = 0 
gas_whheat = 0
gas_cook = 0 
gas_dry = 0
e_heat = 0 
e_whheat = 0
e_cook = 0 
e_dry = 0

config_files=[]
with open('config/appliance_config.csv', newline='') as csvfile : 
	fr = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in fr : 
		if "Total Number of Houses" in row[0] : 
			total_count = int(row[1])/3 #count per phase
		elif 'Appliance Type' in row[0] : 
			continue 
		else :
			gas_heat = total_count*float(row[1])
			gas_whheat = total_count*float(row[2])
			gas_cook = total_count*float(row[3]) 
			gas_dry = total_count*float(row[4])
			e_heat = total_count-gas_heat 
			e_whheat = total_count-gas_whheat 
			e_cook = total_count-gas_cook  
			e_dry = total_count-gas_dry 
			config_file_name = 'elec_config_'+str(row[0]).replace(" ", "_")+'.glm'
			config_files.append(config_file_name)
			fw = open("elec_config/"+config_file_name, 'w')
			fw.write('#define HOUSESPERPHASE=' + str(int(total_count)))
			fw.write('\n#define GAS_HEATING_COUNT=' + str(int(gas_heat))) 
			fw.write('\n#define GAS_WHHEATING_COUNT=' + str(int(gas_whheat))) 
			fw.write('\n#define GAS_COOKING_COUNT=' + str(int(gas_cook))) 
			fw.write('\n#define GAS_DRYING_COUNT=' + str(int(gas_dry))) 
			fw.write('\n#define ELEC_HEATING_COUNT=' + str(int(e_heat))) 
			fw.write('\n#define ELEC_WHHEATING_COUNT=' + str(int(e_whheat))) 
			fw.write('\n#define ELEC_COOKING_COUNT=' + str(int(e_cook))) 
			fw.write('\n#define ELEC_DRYING_COUNT=' + str(int(e_dry))) 

for i,file_name in enumerate(config_files) : 
	if i==0 : # resetting the folder by removing all the model files 
		files = glob.glob('model_files/*')
		for f in files : 
			os.remove(f)
	copyfile('model.glm', 'model_files/model.glm')
	new_file = "model_files/model_"+file_name
	os.rename("model_files/model.glm",new_file)

	with open(new_file, 'r+') as fm:
			content = fm.read()
			fm.seek(0, 0)
			line="#include \"elec_config/" + file_name + "\"" 
			fm.write(line+"\n"+"#define RUN_NAME="+file_name[12:-4]+"\n")
	        


# gridlabd.command("model.glm")
# gridlabd.start("wait")
# quit()












