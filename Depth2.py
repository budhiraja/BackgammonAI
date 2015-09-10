"""
Artificial Intelligence(Spring 2014) Mini Project 1 : Backgammon Simulation

Submitted by:
Amar Budhiraja  (2013030009)
Aman Arora	(201201162)

"""


import random

board_input=[]
z1,z2=0,0
dice=[]
dice_combo=[]

class Node:
	def __init__(self,board):
		"""Constructor"""
		self.child=[]
		self.parent=None
		self.board=board
		self.evaluation=0.0
		self.move=""
		self.bar=[]
 		
def evaluation(node):                        
	''' z1 is Alice's [MAX] OnBarCheckers '''
	C=node.board
	z1=node.bar[0]
	z2=-node.bar[1]
	e=0.0
	sum_ni=0
	sum_mi=0
	sum_pos = z1
	prev = -1
	num_in_hb = 0

	for i in range(len(C)):
		
		if( i>=7 and prev>=2 and C[i]>=2 ):			# Fortification is good
			e += 0.04
		prev = C[i]

		if( C[i] > 0 ):						# Summing positives
			sum_pos += C[i]
			if( i>=19 and i<=23 ):				# Checkers in home state
				num_in_hb +=1

		if( C[i]>1 ):
			sum_ni += 2					# Max's doors
			if ( i>=19 and i<=23 ):
				sum_ni += 1
			if C[i] > 4 :
				sum_ni -= 1

		elif ( C[i]<-1 ):					# Min's doors
			sum_mi -= 2
			if C[i]<-4 :
				sum_mi += 1

	e = 0.01 * (sum_ni + sum_mi)  + 0.029*( z2-z1 )

	if sum_pos < 15 :						# Priority given to bearing off
		e += (15-sum_pos)*0.1

	if (num_in_hb/sum_pos)*100 > 70 and (num_in_hb/sum_pos)*100 != 100:	# Adding Random importance if crossed 70% bench mark
		e += random.random()
	return e


def moveOneDice(root,d):
	child=Node(list(root.board))
	child.bar=list(root.bar)
	child.parent=root
	result=[]
	bear_off=False
	sum_of_pos=child.bar[0]
	sum_of_home=0
	for i in root.board:
		if i>0:
			sum_of_pos+=i
	for i in range(23,17,-1):
		if root.board[i]>0:
			sum_of_home+=root.board[i]
			

	if sum_of_home==sum_of_pos:
		bear_off=True
	if child.bar[0]>0:
		if child.board[d-1]>-2:
			if child.board[d-1]==-1:
				child.bar[1]-=1
				child.board[d-1]=0
			child.bar[0]-=1
			child.board[d-1]+=1	
			child.move=root.move+"Z "+str(d)+'\n'
			result.append(child)
	else:
		if bear_off:
			for i in range(18,24):
				new_bear_child=Node(list(root.board))
				new_bear_child.bar=list(root.bar)
				if i+d==24 and new_bear_child.board[i]>0 :
					new_bear_child.board[i]-=1
					new_bear_child.move=root.move+str(i+1)+" O"+'\n'
					result.append(new_bear_child)



		for i in range(24): # 25 is the Number of points on the Board
			moved=False
			if root.board[i]>0 and i+d < 24:
				new_child=Node(list(root.board))
				new_child.bar=list(root.bar)
				if new_child.board[i+d]>-2:
					if new_child.board[i+d]==-1:
						new_child.board[i+d]=1
						new_child.board[i]-=1
						new_child.bar[1]-=1
						moved=True
					else:
						new_child.board[i+d]+=1
						new_child.board[i]-=1
						moved=True
				if moved:
					new_child.move=root.move+str(i+1)+" "+str(i+d+1)+'\n'
					result.append(new_child)
	return result

def makeMoves(root,dice):
	# Iteration 1 dice[0] followed by dice[1]

	firstMove1=moveOneDice(root,dice[0])
	secondMove1=[]
	if firstMove1:
		for i in firstMove1:
			temp=moveOneDice(i,dice[1])
			for j in temp:
				secondMove1.append(j)

	# Iteration 2 dice[1] followed by dice[0]

	firstMove2=moveOneDice(root,dice[1])
	secondMove2=[]
	if firstMove2:
		for i in firstMove2:
			temp=moveOneDice(i,dice[0])
			for j in temp:
				secondMove2.append(j)
	finalResults=[]
	if secondMove1:
		for i in secondMove1:
			flag=False
			for j in finalResults:
				if i.board==j.board:
					flag=True
			if flag==False:
				finalResults.append(i)
	if secondMove2:
		for i in secondMove2:
			flag=False
			for j in finalResults:
				if i.board==j.board:
					flag=True
			if flag==False:
				finalResults.append(i)
	
	if secondMove1==[] and secondMove2==[]:
		if firstMove2==[]:
			finalResults +=firstMove1
			for i in firstMove1:
				i.move+="pass\n"
		elif firstMove1==[]:
			finalResults+=firstMove2
			for i in firstMove2:
				i.move+="pass\n"

	return finalResults



def rev(node):
	t=[]
	for i in node.board:
		t.append(-i)
	new_node=Node(t)
	new_node.bar.append(-node.bar[1])
	new_node.bar.append(-node.bar[0])
	return new_node

def moveIllegalBear(root,d):
	bear_off=False
	sum_of_pos=root.bar[0]
	sum_of_home=0
	for i in root.board:
		if i>0:
			sum_of_pos+=i
	for i in range(23,17,-1):
		if root.board[i]>0:
			sum_of_home+=root.board[i]
	if sum_of_home==sum_of_pos:
		bear_off=True
	result=[]
	if bear_off:
		for i in range(18,24):
				bear_child=Node(list(root.board))
				bear_child.bar=list(root.bar)
				if i+d>24 and bear_child.board[i]>0:
					bear_child.board[i]-=1
					bear_child.move=root.move+str(i+1)+" O"
					result.append(bear_child)
	if result!=[]:
		return result
	


def makeIllegalBearMove(root,dice):
	firstMove1=moveIllegalBear(root,dice[0])
	secondMove1=[]
	if firstMove1:
		for i in firstMove1:
			temp=moveIllegalBear(i,dice[1])
			for j in temp:
				secondMove1.append(j)

	# Iteration 2 dice[1] followed by dice[0]

	firstMove2=moveIllegalBear(root,dice[1])
	secondMove2=[]
	if firstMove2:
		for i in firstMove2:
			temp=moveIllegalBear(i,dice[0])
			for j in temp:
				secondMove2.append(j)
	finalResults=[]
	if secondMove1:
		for i in secondMove1:
			flag=False
			for j in finalResults:
				if i.board==j.board:
					flag=True
			if flag==False:
				finalResults.append(i)
	if secondMove2:		
		for i in secondMove2:
			flag=False
			for j in finalResults:
				if i.board==j.board:
					flag=True
			if flag==False:
				finalResults.append(i)
	
	if secondMove1==[] and secondMove2==[]:
		if firstMove2==[]:
			finalResults +=firstMove1
			for i in firstMove1:
				i.move+="pass"
		elif firstMove1==[]:
			finalResults+=firstMove2
			for i in firstMove2:
				i.move+="pass"

	return finalResults



def init(board,bar,dice):	# bar[0] is mine and bar[1] is opponent's
	for i in range(1,7):
		for j in range(1,7):
			dice_combo.append([i,j])
	root=Node(board)
	root.bar=bar
	rootResults = makeMoves(root,dice)
	depth1_result=[]
	temp=[]
	temp_evaluation=0.0

	if rootResults==[]:
		rootResults=makeIllegalBearMove(root,dice)

	if rootResults!=[]:
		for i in rootResults:
			depth1_result=[]
			temp_evaluation=0.0
			for j in dice_combo:
				temp=rev(i)
				depth1_result+=makeMoves(temp,j)
			for k in depth1_result:
				temp_evaluation+=evaluation(rev(k))
			i.evaluation=temp_evaluation/len(depth1_result)		
		max_child=rootResults[0]
		for i in rootResults:
			if i.evaluation> max_child.evaluation:
				max_child=i
		if max_child.move!="":
			print max_child.move
		else:
			print "pass\npass"
	else:
		print "pass\npass"

def input():
	str1=raw_input()
	board_input=str1.split(' ')
	for i in range(len(board_input)):
		board_input[i]=int(board_input[i])
	if len(board_input)!=24:
		print "Wrong Number of Board Configs"
		return
	# Taking the Bar as input	
	str2=raw_input()
	#str2=str2.split(' ')
	z1=str2.count('a')
	z2=-(str2.count('b'))

	# Taking the Dice as input

	str3=raw_input()
	str3=str3.split(' ')
	dice.append(int(str3[0]))
	dice.append(int(str3[1]))


	root=Node(board_input)
	root.bar=[z1,z2]

	init(board_input,[z1,z2],dice)



if __name__=='__main__':
	input()
