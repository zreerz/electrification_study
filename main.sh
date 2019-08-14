gridlabd --version
python3 main.py
for filename in model_files/*.glm; do 
	gridlabd "$filename"
done