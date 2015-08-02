# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import operator
def main():
	T= int(raw_input())
	result = []
	assigned_1 = 0
	assigned_2 = 0
	for i in range(1, T+1):
		N,M = raw_input().split()
		N=int(N)
		M=int(M)
		dod = [M/N]*N
		person = 0
		for p in range(1,(M%N)/2+1):
			assigned_1 = min(enumerate(dod), key=operator.itemgetter(1))
			dod[assigned_1[0]] += 1
			print dod
			person+=1
			assigned_2 = min(enumerate(dod[::-1]), key=operator.itemgetter(1))
			dod[len(dod)-1-assigned_2[0]] += 1
			print dod
			person+=1
		if((M%N)==person):
			result.append(str(len(dod)-assigned_2[0])+ ' '+ str(dod[len(dod)-assigned_2[0]-1]-1))

		else:
			if(M%2 == 0):
				assigned_2 = min(enumerate(dod[::-1]), key=operator.itemgetter(1))
				result.append(str(len(dod)-assigned_2[0])+ ' '+ str(dod[len(dod)-assigned_2[0]-1]))
			else:
				assigned_1 = min(enumerate(dod), key=operator.itemgetter(1))
				result.append(str(assigned_1[0]+1)+ ' '+ str(dod[assigned_1[0]]))
		# if(M%2==1):
		# 	assigned_1 = min(enumerate(dod), key=operator.itemgetter(1))
		# 	result.append(str(assigned_1[0]+1)+' '+ str(dod[assigned_1[0]]))
		# else:
		# 	if((M%N)%2 == 0):
		# 		result.append(str(len(dod)-assigned_2[0])+ ' '+ str(dod[len(dod)-assigned_2[0]-1]-1))

	for item in result:
		print item

if __name__ == '__main__':
	main()