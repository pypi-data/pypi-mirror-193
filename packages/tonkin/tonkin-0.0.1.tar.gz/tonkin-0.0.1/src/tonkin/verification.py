def verifyASCII(start, stop, result, source):
	return source[start:stop].decode("ASCII") == result

# Check if the file uses the MDF format
def checkFormat(header):
	return verifyASCII(0, 3, "MDF", header)

# Check if the file uses MDF 3.00
def checkVersion(header):
	return verifyASCII(8, 12, "3.00", header)

# Check if the vendor is Ecotrons
def checkVendor(header):
	return verifyASCII(16, 24, "Ecotrons", header)

# Check if the file was created by EcoCAL
def checkSoftware(header):
	return verifyASCII(100, 106, "EcoCAL", header)

# Check that the second vendor is Ecotrons
def checkSecondVendor(header):
	return verifyASCII(132, 140, "Ecotrons", header)

def checkHeader(header):
	if not checkFormat(header):
		return False
	elif not checkVersion(header):
		return False
	elif not checkVendor(header):
		return False
	elif not checkSoftware(header):
		return False
	elif not checkSecondVendor(header):
		return False
	return True
