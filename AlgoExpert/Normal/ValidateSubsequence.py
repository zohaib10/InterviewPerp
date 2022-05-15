def isValidSubsequence(array, sequence):
    # Write your code here.
	if len(sequence) == 0:
		return True
	
	i = 0;
	j = 0;
	while i < len(array) and j < len(sequence):
		if array[i] == sequence[j]:
			i = i + 1
			j = j + 1
		else:
			i = i + 1
	
	if j == len(sequence):
		return True
	
	return False
	
array=[5,1,22,25,6,-1,8,10]
sequence=[1,6,-10,10]
print(isValidSubsequence(array, sequence))