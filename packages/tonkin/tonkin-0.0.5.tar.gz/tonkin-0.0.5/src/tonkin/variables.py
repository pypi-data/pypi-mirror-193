import tonkin.arrays
import tonkin.data
import tonkin.fixed

# Splits the variable definition section into individual definitions
def _splitVariables(variableSection):
	return tonkin.arrays.splitArrayBySub(variableSection, [0x43, 0x43, 0x3E])

# Extract the name of a variable from the definition
def _extractVariableName(definition):
	outputBytes = []
	# Remove data before variable name
	definition = definition[66:]

	# Extract name
	for i in definition:
		if i == 0x00:
			break
		outputBytes.append(chr(i))

	return "".join(outputBytes)

# Extract names from a list of variable definitions
def _getVariableNames(splitVars):
	# Don't get the "time" variable
	splitVars.pop(-1)
	output = []
	for var in splitVars:
		output.append(_extractVariableName(var))
	return output

# Get the type of a variable from it's inclusion in an A2L file
def _getTypeFromA2LData(variableName, a2lData):
	for i in a2lData:
		rightCategory = i["Category"] == "Measurement"
		rightName = i["Name"] == variableName
		if rightCategory and rightName:
			# The type is stored in "conversion method" after the string "test_CM_"
			# This removes that prefix
			rawType = i["Conversion Method"]
			varType = rawType[8:]

			return varType
	raise ValueError("Variable " + variableName + " not found in A2L data")

# Take a list of variable names and return a list of variable dicts with types
def _getTypesFromA2LData(variableNames, a2lData):
	output = []
	for variable in variableNames:
		currentVar = {
			"Name": variable,
			"Type": _getTypeFromA2LData(variable, a2lData)
		}
		output.append(currentVar)
	return output

# Given a data type, return it's length in bytes
def getTypeLength(typeName):
	# If the typeName is a dictionary, meaning it's a fixdt
	if "fix" in typeName:
		return tonkin.fixed.getByteLengthFromName(typeName)
	return tonkin.data.typeLengths[typeName]

# Given a variable with a type, return the length of the variable in bytes
def _getVariableLength(variable):
	return getTypeLength(variable["Type"])

# Given a list of variable dicts, returns a list of variable dicts with types
def _getVariableLengths(variables):
	output = []
	for var in variables:
		var["Length"] = _getVariableLength(var)
		output.append(var)
	return output

# Given a variable section and data from an A2L file, return a list of dicts
# representing the variables, including types and lengths in bytes
def getVariableListFromA2L(variableSection, a2lData):
	split = _splitVariables(variableSection)
	names = _getVariableNames(split)
	namesWithTypes = _getTypesFromA2LData(names, a2lData)
	namesWithTypesAndLengths = _getVariableLengths(namesWithTypes)
	# Add the "time" variable present in all files
	namesWithTypesAndLengths.append({"Name": "time", "Type": "single", "Length": 4})
	return namesWithTypesAndLengths
