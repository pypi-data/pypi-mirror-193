import tonkin.fileops
import countach
import tonkin.wholedata
import tonkin.variables
import tonkin.dataStream
import tonkin.packets
import csv

# Given a dat file and an a2l file, returns a list of dicts
# each representing a single packet
def readDatFileWithA2L(datFile, a2lFile):
	# Import the files
	a2lData = countach.extractData(a2lFile)
	fileBytes = tonkin.fileops.importFile(datFile)
	# Split the dat file up into sections
	header, vars, stream = tonkin.wholedata.splitFileData(fileBytes)
	# Extract the variables from the variable section
	variableList = tonkin.variables.getVariableListFromA2L(vars, a2lData)
	rawPackets = tonkin.dataStream.splitStreamToPackets(stream, variableList)
	output = []
	variableList.reverse()
	for packet in rawPackets:
		output.append(tonkin.packets.readRawPacket(packet, variableList))
	return output

def datFileTo2DArrayA2L(datFile, a2lFile):
	data = readDatFileWithA2L(datFile, a2lFile)
	output = []
	
	# Get headers
	headers = []
	for key in data[0]:
		headers.append(key)
	output.append(headers)

	
	for packet in data:
		row = []
		for key in packet:
			row.append(packet[key])
		output.append(row)
	return output

def datFileToCSVWithA2L(datFile, a2lFile, csvFile, delimiter=","):
	twoD = datFileTo2DArrayA2L(datFile, a2lFile)
	with open(csvFile, "w+") as f:
		csvWriter = csv.writer(f, delimiter=delimiter)
		csvWriter.writerows(twoD)
