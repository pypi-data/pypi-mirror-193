import struct
import tonkin.fixed

def _convertint8(int8B):
	return int.from_bytes(int8B, "little", signed=True)

def _convertint16(int16B):
	return int.from_bytes(int16B, "little", signed=True)

def _convertint32(int32B):
	return int.from_bytes(int32B, "little", signed=True)

def _convertuint8(uint8B):
	return int.from_bytes(uint8B, "little", signed=False)

def _convertuint16(uint16B):
	return int.from_bytes(uint16B, "little", signed=False)

def _convertSingle(singleB):
	return struct.unpack("f", singleB)[0]

def _convertBoolean(boolB):
	if boolB == b'\x01':
		return True
	else:
		return False

def _convertFixed(fixedB, rawVarType):
	signed, length, _, _ = tonkin.fixed.getFixedType(rawVarType)
	rawValue = tonkin.fixed.chopExtraBits(fixedB)
	if signed == 1:
		rawValue -= 2 ** length
	return rawValue

# Given a series of bytes representing a value within a packet
# and a variable dict, return the value of the 
def readRawValue(rawValue, var):
	varType = var["Type"]
	
	if varType == "int8":
		return _convertint8(rawValue)
	elif varType == "int16":
		return _convertint16(rawValue)
	elif varType == "int32":
		return _convertint32(rawValue)
	elif varType == "uint8":
		return _convertuint8(rawValue)
	elif varType == "uint16":
		return _convertuint16(rawValue)
	elif varType == "single":
		return _convertSingle(rawValue)
	elif varType == "boolean":
		return _convertBoolean(rawValue)
	elif "fix" in varType:
		return _convertFixed(rawValue, varType)
