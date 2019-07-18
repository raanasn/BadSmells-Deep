import redis
from graph import *
from entropy import *
from outputCreator import *
from lcom import *
from badSmell import*
from parse2 import *

import ast

def generate():
	### calculates Lcom and LcomHS
	path1=['Junit/BadSmells/1.txt', 'Ganttproject/BadSmells/1.txt','Mockito/BadSmells/1.txt']
	path2=["Junit/BadSmells/2.txt",'Ganttproject/BadSmells/2.txt','Mockito/BadSmells/2.txt']
	path3=["Junit/BadSmells/3.txt",'Ganttproject/BadSmells/3.txt','Mockito/BadSmells/3.txt']
	parse_file=['Junit1.2.xmi','Ganttproject1.2.xmi','Mockito1.2.xmi']
	outputs=['Junit_output.txt','Ganttproject_output.txt','Mockito_output.txt']
	x_all=[]
	y_all=[]
	z_all=[]
	badSmells_number=[]
	#i=0
	for item1,item2,item3,pf,out in zip(path1,path2,path3,parse_file,outputs):
		classList=parseXMI(pf)
		badSmells, len_featureEnvy=getBadSmell(item1,item2,item3) 	
		L=get_lcom(classList)
		x,y,y_badSmells=get_data(L,badSmells,out,len_featureEnvy)
		x_all=x_all+x
		y_all=y_all+y
		badSmells_number=badSmells_number+y_badSmells
		#z_all=z_all+([i]* len(x_all))
		#i=i+1
		z_all.append(len(x_all))
	return x_all,y_all,z_all,badSmells_number

