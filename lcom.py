def get_lcom(classList):
	#3th is attr_count, 4th is ope_count, 5th is usedFunc
	answer=[]
	i=0
	for item in classList:
		answer.append([])
		F=float(item[3])
		M=float(item[4])
		MyF=float(item[5])
		try:
			lcom=1-((1/(F*M))*MyF)
		except:
			lcom=100
		try:
			lcomHS=(1/(M-1))*(M-((1/F)*MyF))
		except:
			lcomHS=100
		answer[i].append(lcom)
		answer[i].append(lcomHS)
		i=i+1
	return answer
