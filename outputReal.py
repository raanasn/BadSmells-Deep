import redis
from graph import *
from entropy import *
from outputCreator import *
from lcom import *

import ast

def generate():
	#redis
	redisLists = redis.StrictRedis(host='localhost',port=6379, db=0)
	classList=ast.literal_eval(redisLists.lpop('ClassList'))
	relation=ast.literal_eval(redisLists.lpop('RelationList'))
	packageList=ast.literal_eval(redisLists.lpop('PackageList'))
	packageRelation=ast.literal_eval(redisLists.lpop('PackageRelation'))
	allRelFunc=ast.literal_eval(redisLists.lpop('AllRelFunc'))
	counterOfRel=ast.literal_eval(redisLists.lpop('CounterOfRel'))
	badSmells=ast.literal_eval(redisLists.lpop('BadSmells'))
	#print 'newRelationList',newRelationList
	#print 'updatedRelations',updatedRelations

	### get critical
	### cri: return critical classes in a list
	cri=get_critical(relation,classList)
	#print 'critical classes are: ',cri,'\n'

	### graph-properties
	### atr: return all class attributes in a list: Number, ID, Name, Degree C., InDegree C., OutDegree C. Betweenness C., Load C., Centrality C.-deleted
	### rel: returns all edge attributes in a list: RelationName, ID-edge1, ID-edge2, Nr.Edge1, Nr. Edge2, in this case it works like relation-deleted 
	G=get_graphAttributes(relation,classList)
	#print 'attribute of each class is: ',atr,'\n'

	### calculates Lcom and LcomHS 	
	L=get_lcom(classList)

	### calculate entropy
	### ent: returns a list with values that represent how important a class is
	ent=get_entropy(relation,classList)

	### get output-textfile for graph-attributes (+ edge-betweenness)
	get_output(classList,relation,cri,G,ent,L)
	#x,y=get_data(classList,relation,cri,G,ent,L,badSmells)
	
	redisLists.lpush('ClassList', classList)
	redisLists.lpush('RelationList', relation)
	redisLists.lpush('PackageList', packageList)
	redisLists.lpush('PackageRelation', packageRelation)
	redisLists.lpush('AllRelFunc', allRelFunc)
	redisLists.lpush('CounterOfRel', counterOfRel)
	redisLists.lpush('BadSmells', badSmells)
	#return x,y

generate()
