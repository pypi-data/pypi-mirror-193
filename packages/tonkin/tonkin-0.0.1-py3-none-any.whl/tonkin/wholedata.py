import arrays

def extractHeaderSec(fileBytes):
	return fileBytes[0:228]

def extractVariablesSec(fileBytes):
	output = fileBytes[228:]
	end = arrays.getSubArrayIndex(output, [0x43, 0x47, 0x1A])
	return output[:end]

def extractDataStream(fileBytes, prePrepared=False):
	# Remove the header and variable definition sections
	# if it hasn't been done already
	if prePrepared:
		output = fileBytes
	else:
		headerLength = len(extractHeaderSec(fileBytes))
		variableLength = len(extractVariablesSec(fileBytes))
		upperLength = headerLength + variableLength
		output = fileBytes[upperLength:]

	# The sequence of bytes that marks the start of the data stream
	startMarker = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
	# The index of the first byte of the data stream
	start = arrays.getSubArrayIndex(output, startMarker) + 1
	
	return output[start:]

def splitFileData(fileBytes):
	header = extractHeaderSec(fileBytes)
	variables = extractVariablesSec(fileBytes)
	# Chop the upper sections away
	upperLength = len(header) + len(variables)
	fileBytes = fileBytes[upperLength:]
	dataStream = extractDataStream(fileBytes, prePrepared=True)
	return header, variables, dataStream
