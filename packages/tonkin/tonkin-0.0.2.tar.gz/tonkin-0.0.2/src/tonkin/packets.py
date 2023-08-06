import values

# Given a series of bytes representing a packet and
# a list of variable dicts, return a list of bytestrings
# representing variable values for the packet
def _splitPacket(rawPacket, vars):
	splitPacket = []
	for var in vars:
		splitPacket.append(rawPacket[:var["Length"]])
		rawPacket = rawPacket[var["Length"]:]
		
	return splitPacket

# Given a series of bytes representing a packet,
# return a dictionary representing the packet
def readRawPacket(rawPacket, vars):
	vals = _splitPacket(rawPacket, vars)
	packet = {}
	for index, var in enumerate(vars):
		varName = var["Name"]
		value = values.readRawValue(vals[index], var)
		packet[varName] = value
	return packet
