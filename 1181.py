import sys 
	
	word_dict = dict() 
	
	for _ in range(int(sys.stdin.readline())):
		word = input()
		word_dict[word] = len(word)
		
	word_dict = sorted(word_dict.items() , key=lambda x : (x[1],x[0]))
	
	for x in word_dict:
		print(x[0])
