def NULL_not_found(object: any) -> int:
	objectType = type(object)
	if object is None:
		typeName = 'Nothing'
	elif objectType is float and object != object:
		typeName = 'Cheese'
	elif object == 0 and objectType is int:
		typeName = 'Zero'
	elif object == '':
		typeName = 'Empty'
	elif object is False:
		typeName = 'Fake'
	else:
		typeName = 'Type not found'

	if typeName == 'Type not found':
		print(typeName)
		return 1
	print(f'{typeName}: {object} {objectType}')
	return 0