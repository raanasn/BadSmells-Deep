import networkx as nx
def get_output(classList,relation,critical,G,ent,L):
	#creating output file:
	f=open("output.txt",'w')
	i=0
	#f.write("Number"+" "+"ID"+" "+"Name"+" "+"Degree-C."+" "+"In-Degree-C."+" "+"Out-Degree-C"+" "+"Betweeness-C."+" "+"Load-C."+" "+"Closeness-C."+" "+"Lcom"+" "+"LcomHR"+" "+"IsCritical"+" "+"Entropy"+" "+"\n")
	for item in classList:
		if G.has_node(i):
			f.write(str(item[2])+ " "+str(item[0])+" "+str(item[1])+" "+str(nx.degree_centrality(G)[i])+" "+str(nx.in_degree_centrality(G)[i])+" "+str(nx.out_degree_centrality(G)[i])+" "+str(nx.betweenness_centrality(G)[i])+" "+str(nx.load_centrality(G)[i])+" "+ str(nx.closeness_centrality(G)[i])+" "+str(L[i][0])+" "+str(L[i][1]))
		if G.has_node(i)==False:
			f.write(str(item[2])+ " "+str(item[0])+" "+str(item[1])+" "+str(0)+" "+str(0)+" "+str(0)+" "+str(0)+" "+str(0)+" "+ str(0)+" "+str(0)+" "+str(0))
		if item[2] in critical:
			f.write(" "+"***")
		else:
			f.write(" "+"#")
		f.write(" "+str(ent[i][1]))
		f.write("\n"+"\n")
		i=i+1
	i=0
	#f.write("Relation"+" "+"ID-edge1"+" "+"ID-edge2"+" "+"Nr. Edge1"+" "+"Nr.Edge2"+"\n")
	#for item in relation:
	#	f.write(str(item[0])+" "+str(item[1])+" "+str(item[2])+" "+str(item[3])+" "+ str(item[4])+"\n"+"\n")
	#f.write("###############################################\n\n")
	#f.write("Edge-Betweenness-C.: \n")
	#for item in relation:
	#	if G.has_node(i):
	#		f.write(str(nx.edge_betweenness_centrality(G).items()[i])+" "+"\n")
	#	else:
	#		f.write(str(0)+" "+"\n")
	#	i=i+1
	#f.write("\n###############################################\n\n")
	#f.write("Closeness Centrality of Graph:"+" "+ str(nx.closeness_centrality(G,True)))
	f.close() 

def get_data(L,badSmells,out,featureEnvy):
	x=[]
	y=[]
	y_all=[]
	i=0
	f=open(out,'r')
	for item in f:
		word=item.split()
		if word!=[]:
			x.append([])
			x[i].extend([float(word[3]),float(word[4]),float(word[5]),float(word[6]),float(word[7]),float(word[8]),float(word[9]),float(word[10])])
			if word[11] =="***":
				x[i].append(1)
			else:
				x[i].append(0)
			if float(word[12]) < 100:
				x[i].append(word[12])
			else:
				x[i].append(100)
			if str(word[2]) in badSmells or float(word[12])>100:
				y.append(1)
				if str(word[2]) in badSmells[:featureEnvy]:
					y_all.append(1)
				elif str(word[2]) in badSmells[featureEnvy:]:
					y_all.append(2)
				else:
					y_all.append(3)
			else:
				y.append(0)
				y_all.append(0)
			i=i+1
	return x,y,y_all




