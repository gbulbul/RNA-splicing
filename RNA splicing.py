dna_string='ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG'
#print(len(dna_string))
introns={
'intron1':'ATCGGTCGAA', 
'intron2':'ATCGGTCGAGCGTGT'}
rna_codons = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'s', 'UCA':'S', 'UCG':'S',
'UAU':'Y', 'UAC':'Y', 'UAA':'STOP', 'UAG':'STOP',
'UGU':'C', 'UGC':'C', 'UGA':'STOP', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'}
#dna_string=dna_string.replace("T","U")
protein=''
def introns_to_lens(introns):
    lens=()   
    for key in introns.keys():
        lens+=(len(introns[key]),)   
    return lens
#print(introns_to_lens(introns))
lens=(m,n)=introns_to_lens(introns)
for j in range(0,2,1):
    for i in range(0,len(dna_string)):
        for key_introns in introns.keys():
            #print(dna_string[i:i+lens[j]])
            if list(introns)[j]==key_introns and dna_string[i:i+lens[j]]==introns[key_introns] :
               dna_string=dna_string.replace(dna_string[i:i+lens[j]],"")
dna_string=dna_string.replace("T","U")
print(dna_string)
for i in range(0,len(dna_string),3):                
   for key_codons in rna_codons.keys():
       if dna_string[i:i+3]==key_codons:
          while rna_codons[key_codons]!='STOP':
                protein+=rna_codons[key_codons]
                print(protein)
                break
         