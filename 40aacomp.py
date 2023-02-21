# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use 20 named variables
# Variation: use a list
import gzip
import sys
import mcb185
A = 0
C = 0
D = 0
E = 0
F = 0
G = 0
H = 0
I = 0
K = 0
L = 0
M = 0
N = 0
P = 0
Q = 0
R = 0
S = 0
T = 0
V = 0
W = 0
Y = 0

with gzip.open(sys.argv[1],'rt') as fp:
	for line in fp.readlines():
		if line.startswith('>'):continue
		#print(line, end='')
		A += line.count('A')
		C += line.count('C')
		D += line.count('D')
		E += line.count('E')
		F += line.count('F')
		G += line.count('G')
		H += line.count('H')
		I += line.count('I')
		K += line.count('K')
		L += line.count('L')
		M += line.count('M')
		N += line.count('N')
		P += line.count('P')
		Q += line.count('Q')
		R += line.count('R')
		S += line.count('S')
		T += line.count('T')
		V += line.count('V')
		W += line.count('W')
		Y += line.count('Y')
	print('A', A, f'{A/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('C', C, f'{C/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('D', D, f'{D/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('E', E, f'{E/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('F', F, f'{F/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('G', G, f'{G/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('H', H, f'{H/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('I', I, f'{I/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('K', K, f'{K/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('L', L, f'{L/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('M', M, f'{M/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('N', N, f'{N/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('P', P, f'{P/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('Q', Q, f'{Q/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('R', R, f'{R/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('S', S, f'{S/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('T', T, f'{T/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('V', V, f'{V/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('W', W, f'{W/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')
	print('Y', Y, f'{Y/(A+C+D+E+F+G+H+I+K+L+M+N+P+Q+R+S+T+V+W+Y):.4f}')


"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
