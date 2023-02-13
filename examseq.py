import random
n = 20
x = .5203
seq = ''
# generate random sequence
for i in range(n):
	r = random.random()
	if r < x: seq += random.choice('CG')
	else:     seq += random.choice('AT')
print(seq)

# count letters
a = 0 
c = 0
g = 0 
t = 0
for i in range(len(seq)):
	if   seq[i] == 'A': a += 1
	elif seq[i]	== 'T': t += 1
	elif seq[i]	== 'C': c += 1 
	else:               t += 1
	
print(a/len(seq), c/len(seq), glen(seq), t/len(seq))

#K-mer
print(seq)
k = 3
for i in range(len(sqe) -k +1):
	#check if palindrome
	k2 = k//2
	kmer = seq[i:i+k]
	first = kmer[:k2]
	second = kmer[:k2]
	rc = ''
	for nt in second
		if nt == 'A': rc = 'T'
	print(kmer, kmer[:k], kmer[-k2:])
	
# palindroms
k2 = k // 2
print(k2)
print(seq[0:2] seq[-2:])