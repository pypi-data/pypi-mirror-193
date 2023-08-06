def importFile(fileName):
	output = None
	with open(fileName, "rb") as file:
		output = bytearray(file.read())
	return output
	
