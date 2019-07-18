import redis
from parse import *
from counterOfRelation import*
from badSmell import*
from badSmell import*

#redis
redisLists = redis.StrictRedis(host='localhost',port=6379, db=0)

### set xmi-file
### if not readed from xml file: 
### new classes must be added (or removed) in classList: [['IDName','NameOfClass','Number']] (Number is unic and an integer that is added/ IDName is the ID in the xml-file, it can be same with Number)
### new relations must be added (or removed) in relation: [['AssociationName','IDName1','IDName2','Number of first class','Number of second class']]
### new package-list must be added (or removed) in packageList: [['IDNameOfPackage','NameOfPackage','IDNameofClass1','IDNameofClass2',....,'Number']]
### new package-relations must be added (or removed) in packageRelations: [['IDNameOfPackage1','IDNameOfPackage2']]
relation, classList, packageList, packageRelation=parseXMI('Junit1.2.xmi')
#print 'relation-list: ',relation,'\n'
#print 'package-relation',packageRelation
#print 'package-list',packageList,'\n'
#print 'class-list: ',classList,'\n'

### allRelFunc: get all Relations with the Caller and Callee Functions: [nameOfClass1,nameOfClass2, Caller-Function in Class1, Caller-Function in Class2]
### counterOfRel: get all Relations with number in a dictionary: *key of dict* => list of classes: [nameOfClass1,nameOfClass2] *value of dict* => counter of each relation: int
### some of the classes are dynamic. The functions coudn't be extracted!
allRelFunc, counterOfRel=counterOfRelation("JunitClassRelation.txt")
#print 'all relations with function calls: ',allRelFunc,'\n'
#print 'all counted relations: ',counterOfRel,'\n'

###Get Labeled Bad Smell from IPlasma
path1='Junit/BadSmells/1.txt'
path2="Junit/BadSmells/2.txt"
badSmells=getBadSmell(path1,path2)

redisLists.lpush('ClassList', classList)
redisLists.lpush('RelationList', relation)
redisLists.lpush('PackageList', packageList)
redisLists.lpush('PackageRelation', packageRelation)
redisLists.lpush('AllRelFunc', allRelFunc)
redisLists.lpush('CounterOfRel', counterOfRel)
redisLists.lpush('BadSmells', badSmells)
#for printing List:
#while(redisLists.llen('ClassList')!=0):
#	print(redisLists.lpop('ClassList'))


