import arrays

def _calculatePacketLength(vars):
	length = 0
	for var in vars:
		length += var["Length"]
	return length

# Given a data stream and the list of variable types,
# get a list of packets from the data stream
def splitStreamToPackets(stream, vars):
	packetLength = _calculatePacketLength(vars)
	return arrays.splitArrayIntoLengths(stream, packetLength)
