# ELECTRIFICATION STUDY 

## Configuration 
The configuration files are located in `config/`
`config/default.glm` loads the default parameters if `config/local.glm` is not found. 
`config/local.glm` overwrites and appends to `config/default.glm`. Here you can define the start time, stop time and Weather location of the simulation. 
`config/appliance_config.csv` allows to define the number of total houses to be simulated and the percent of the load that is electrified broken down on per appliance basis. 
Multiple lines will result in multiple simulation runs. 

## Running the model 
To run the model: 
~~~
sh main.sh
~~~

## Output
The output from all the defined run in configuration will appear in `output/` folder.
