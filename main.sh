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
python3 main.py
for filename in model_files/*.glm; do 
	gridlabd "$filename"
done
