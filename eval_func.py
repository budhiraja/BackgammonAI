import random
def eval( C,z1,z2 ):                        
	''' z1 is Alice's [MAX] OnBarCheckers '''
	#print C,z1,z2
	sum_ni=0
	sum_mi=0
	sum_pos = z1
	prev = -1
	num_in_hb = 0
	e = 0

	for i in range(len(C)):
		
		if( i>=1 and prev>=2 and C[i]>=2 ):			# Fortification is good
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
		e += (15-sum_pos)

	if (num_in_hb/sum_pos)*100 > 70 and (num_in_hb/sum_pos)*100 !=100:	# Adding Random importance if crossed 70% bench mark
		e += random.random()
	return e

C1 = [1,0,2,-1,0,0,0,0,-4,-1,-2,-5,5,1,0,2,0,0,1,0,-2,0,0,0]
z11=3
z12=0
C2 = [3, 0, 2, -2, -1, -1, 3, -3, 0, 0, 0, 0, 5, -7, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
z21=1
z22=0
C3 = [3, 1, 1, -2, -1, -1, 3, -3, 0, 0, 0, 0, 5, -7, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
z31=1
z32=1
C4 = [2, 2, 1, -2, -1, -1, 3, -3, 0, 0, 0, 0, 5, -7, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0]
z41 =1
z42 =0

C5 = [0 ,0 ,0 ,-2 ,-2 ,-1 ,0 ,-3 ,0 ,0, 0 ,0 ,0 ,-7 ,0 ,-1 ,0 ,0 ,3 ,3 ,3 ,3 ,2 ,1]
z51=0
z52=0

C6 = [0 ,0 ,0 ,-2 ,-2 ,-1 ,0 ,-3 ,0 ,0 ,0 ,0 ,0 ,-7 ,0 ,-1 ,0 ,0 ,3 ,3 ,3 ,1 ,2 ,3]
z61=0
z62=0
C7 = [0, 0 ,0 ,-2, -2 ,-1, 0 ,-3, 0 ,0 ,0 ,0 ,0, -7 ,0 ,-1 ,0 ,0, 3 ,3 ,3 ,3 ,0 ,2]
z71=0
z72=0
C8 = [0, 0, 0 ,-2, -2, -1, 0, -3 ,0 ,0 ,0 ,0 ,0, -7, 0 ,-1, 0, 0, 3, 3, 3, 2, 1 ,2]
z81=0
z82=0
print eval(C5,z51,z52)
print eval(C6,z61,z62)
print eval(C7,z71,z72)
print eval(C8,z81,z82)
