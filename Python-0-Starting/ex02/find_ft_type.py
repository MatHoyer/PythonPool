def all_thing_is_obj(object: any) -> int:
	typeNames = {
		list: 'List',
		tuple: 'Tuple',
		set: 'Set',
		dict: 'Dict',
		str: 'str'
	}
	objectType = type(object)
	typeName = typeNames.get(objectType, 'Type not found')
 
	if typeName == 'str':
		print(f'{object} is in the kitchen : {objectType}')
	elif typeName != 'Type not found':
		print(f'{typeName} : {objectType}')
	else:
		print(typeName)
	return 42