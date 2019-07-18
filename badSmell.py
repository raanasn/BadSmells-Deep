def getBadSmell(path1,path2,path3):
	badSmell=[]
	featureEnvy=0
	with open(path1,'rU') as myF:
		next(myF)
		for line in myF:
			if '0' not in line:
				l2=repr(line.replace("'",""))
				badSmell.append(l2.split("\\")[0])

	with open(path2,'rU') as myF:
		for line in myF:
			if '{}' not in line:
				l2=repr(line.replace("'",""))
				badSmell.append(l2.split("\\")[0])
	featureEnvy=len(badSmell)
	with open(path3,'rU') as myF:
		next(myF)
		for line in myF:
			if 'true' in line:
				l2=repr(line.replace("'",""))
				badSmell.append(l2.split("\\")[0])
	badSmell = [item.replace("'","") for item in badSmell]
	return badSmell, featureEnvy
