codon_lists = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP',
}
def proteins(strand):
    lists=[]
    acids=[]
    for str in range(0,len(strand),3):
        lists.append(strand[str:str+3])
    for protein in lists:
        if codon_lists[protein] == 'STOP':
            break;
        else:
            acids.append(codon_lists[protein])
    return acids
        


