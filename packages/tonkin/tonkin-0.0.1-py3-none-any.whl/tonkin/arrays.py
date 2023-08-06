def shiftArrayLeft(array, shift):
	# Bring large numbers down to smaller equivalents
	# and handle negatives for shifts right
	shift = shift % len(array)

	for i in range(0, shift):
		array.append(array.pop(0))
	return array

# Given a source array and a target array, returns the index of where the target
# array appears within the source array (returns the index of the final value)
def getSubArrayIndex(source, target):
	# TODO: Ensure that the buffer items don't appear in split
	buffer = [None] * len(target)
	
	for j, i in enumerate(source):
		buffer = shiftArrayLeft(buffer, 1)
		buffer[-1] = i

		if buffer == target:
			return j
	
	raise ValueError("Sub-array not found")

def getSubArrayIndices(source, target):
	output = []
	
	# TODO: Ensure that the buffer items don't appear in split
	buffer = [None] * len(target)
	
	for j, i in enumerate(source):
		buffer = shiftArrayLeft(buffer, 1)
		buffer[-1] = i

		if buffer == target:
			output.append(j)
	
	return output

# TODO: Test for different first elements of source
def splitArrayBySub(source, target):
	output = []
	indices = getSubArrayIndices(source, target)
	
	# The case where the target does not appear
	if indices == []:
		return [source]

	for j, i in enumerate(indices):
		startOfBlock = i - len(target) + 1
		
		if j < len(indices) - 1:
			endOfBlock = indices[j+1] - len(target) + 1
		else:
			endOfBlock = len(source)

		output.append(source[startOfBlock:endOfBlock])

	return output

def splitArrayIntoLengthsGen(array, lengths):
	for i in range(0, len(array), lengths):
		yield array[i:i + lengths]

def splitArrayIntoLengths(array, lengths):
	return list(splitArrayIntoLengthsGen(array, lengths))
