import itertools
import sys
import operator
import re
import numpy
import math
def perms(elements):
    if len(elements) <= 1:
        return elements  # Only permutation possible = no permutation
    else:
        # Iteration over the first element in the result permutation:
        for (index, first_elmt) in enumerate(elements):
            other_elmts = elements[:index]+elements[index+1:]
            for permutation in perms(other_elmts): 
                return str([first_elmt]) + permutation

def main():
	T= int(raw_input())
	main_res = []
	for i in range(1,T+1):
		results = []
		num = int(raw_input())
		list_perms = perms(range(1,num+1))
		
		for p in list_perms:
			if False in [x+y<=num+1 for x,y in zip(p,p[1:])]:
				pass
			else:
				results.append(p)
		#lexicographic checking
		# for li in results:
		main_res.append(sorted(results)[0])

	for item in main_res:
			m = re.findall('(\d)',str(item))
			str1 = ' '.join(str(e) for e in m)
			print str1



if __name__ == '__main__':
	main()
