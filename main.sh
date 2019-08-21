gridlabd --version
### Check if a directory does not exist ###
if [ ! -d "model_files/" ] 
then
    mkdir model_files
fi
if [ ! -d "output/" ] 
then
    mkdir output
fi
if [ ! -d "elec_config/" ] 
then
    mkdir elec_config
fi
if [ ! -d "paneldump/" ] 
then
    mkdir paneldump
fi
python3 main.py
for filename in model_files/*.glm; do 
	gridlabd "$filename"
done
python3 post_process.py
