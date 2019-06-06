import subprocess
cmdCommand = "python 2to3_converter.py"
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
