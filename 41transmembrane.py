# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane
import sys
import mcb185

#function for average KD score
def ave_hydrophobicity(reading_frame): #defining the function here
	hydrophobicity = 0
	amino_acids = 'ACDEFGHIKLMNPQRSTVWY' #this is a string
	kd_score = [1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6, -3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3] #this is a list

#for loop, go through each amino acid within the reading frame
	for aa in range(len(reading_frame)): 
#going through the list of amino acids and add the appropriate kd score
		hydrophobicity += kd_score[amino_acids.find(reading_frame[aa])] 
	return hydrophobicity/len(reading_frame) #return the average hydrophobicity 

#function for transmembrane 
def hydro_region(seq, f, t):
	for i in range(len(seq) - f + 1): 
		frame = seq[i : i + f]
		
		if 'P' in frame: continue #proline will not be in transmembrane
		elif ave_hydrophobicity(frame) < t: continue
		else:
				return True
	return False
	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if hydro_region(seq[0:30], 8, 2.5) and hydro_region(seq[30:], 11, 2.0):
		print(defline)



"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
