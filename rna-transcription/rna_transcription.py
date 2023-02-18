def to_rna(dna_strand):
    rna=""
    for char in dna_strand:
        if char == 'G':
            rna=rna+"C"
        elif char == 'C':
            rna=rna+"G"
        elif char == 'T':
            rna=rna+"A"
        elif char == 'A':
            rna=rna+"U"
    return rna
            
