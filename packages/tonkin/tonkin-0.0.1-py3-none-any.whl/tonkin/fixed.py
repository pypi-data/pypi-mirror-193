def _checkIfFixedIsSigned(typeString):
	if typeString[0] == "u":
		signed = 0
	elif typeString[0] == "s":
		signed = 1
	else:
		raise ValueError("Sign indication not found in type string")
	return signed

def _getWordLength(typeString):
	# Remove unneccessary data
	typeString = typeString[4:]
	typeString = typeString.split("_")
	return int(typeString[0])

# TODO: Check if negative total slopes possible?
def _getTotalSlope(typeString):
	totalSlope = 1
	if "S" in typeString:
		totalSlopeIndex = typeString.index("S") + 1
		totalSlope = int(typeString[totalSlopeIndex])
	elif "E" in typeString:
		totalSlopeIndex = typeString.index("E") + 1
		totalSlope = 2 ** int(typeString[totalSlopeIndex])
	return totalSlope

# TODO: Check if negative biases possible?
def _getBias(typeString):
	bias = 0
	if "B" in typeString:
		biasIndex = typeString.index("B") + 1
		bias = int(typeString[biasIndex])
	return bias

def getFixedType(typeString):
	signed = _checkIfFixedIsSigned(typeString)
	wordLength = _getWordLength(typeString)
	totalSlope = _getTotalSlope(typeString)
	bias = _getBias(typeString)
	return signed, wordLength, totalSlope, bias
	
# Round n up to the nearest multiple
def roundUp(n, multiple):
	if multiple == 0:
		return n
	
	remainder = n % multiple
	
	if remainder == 0:
		return n

	return n + multiple - remainder

def getByteLength(bitLength):
	totalBits = roundUp(bitLength, 8)
	return totalBits / 8

def getByteLengthFromName(typeName):
	_, wordLength, _, _ = getFixedType(typeName)
	return getByteLength(wordLength)

# Remove the extra bits from the start of a fixdt value
def chopExtraBits(value, wordLength, byteLength):
	# The case where the wordLength is a multiple of 8
	if wordLength / 8 == byteLength:
		return value
	
	bitsToChop = (byteLength * 8) - wordLength
	binary = bin(value)
	# Chop an extra 2 chars for "0b"
	chopped = binary[bitsToChop + 2:]
	return int(chopped)
