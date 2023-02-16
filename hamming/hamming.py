def distance(strand_a, strand_b):
    count=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        code=0
        while code<len(strand_a):
            if strand_a[code]==strand_b[code]:
                code+=1
            else:
                count+=1
                code+=1
    return count
