def find(search_list, value):
    start=0
    end=len(search_list)
    while start<end:
        mid=(start+end)//2
        if value<search_list[mid]:
            end-=1
        elif value>search_list[mid]:
            start+=1
        else:
            return mid
    raise ValueError("value not in array")
   
    
