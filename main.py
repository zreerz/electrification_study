import csv 
import gridlabd

total_count = 10

gas_heat = 0 
gas_whheat = 0
gas_cook = 0 
gas_dry = 0
e_heat = 0 
e_whheat = 0
e_cook = 0 
e_dry = 0

config_files=[]
with open('appliance_config.csv', newline='') as csvfile : 
	fr = csv.reader(csvfile, delimiter=',', quotechar='|')
	next(fr)
	for row in fr : 
		gas_heat = total_count*float(row[1])
		gas_whheat = total_count*float(row[2])
		gas_cook = total_count*float(row[3]) 
		gas_dry = total_count*float(row[4])
		e_heat = total_count-gas_heat 
		e_whheat = total_count-gas_whheat 
		e_cook = total_count-gas_cook  
		e_dry = total_count-gas_dry 
		config_file_name = 'elec_config_'+str(row[0])+'.glm'
		config_files.append(config_file_name)
		fw = open(config_file_name, 'w')
		fw.write('#define GAS_HEATING_COUNT=' + str(int(gas_heat))) 
		fw.write('\n#define GAS_WHHEATING_COUNT=' + str(int(gas_whheat))) 
		fw.write('\n#define GAS_COOKING_COUNT=' + str(int(gas_cook))) 
		fw.write('\n#define GAS_DRYING_COUNT=' + str(int(gas_dry))) 
		fw.write('\n#define ELEC_HEATING_COUNT=' + str(int(e_heat))) 
		fw.write('\n#define ELEC_WHHEATING_COUNT=' + str(int(e_whheat))) 
		fw.write('\n#define GAS_HEATING_COUNT=' + str(int(e_cook))) 
		fw.write('\n#define ELEC_DRYING_COUNT=' + str(int(e_dry))) 


gridlabd.command("model.glm")
gridlabd.start("wait")
quit()












