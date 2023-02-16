def find_anagrams(word, candidates):
    anagam_list=[]
    for candidate in candidates:
        if candidate.lower() != word.lower():
            if sorted(candidate.lower()) == sorted(word.lower()):
              anagam_list.append(candidate)
    return anagam_list 
                
