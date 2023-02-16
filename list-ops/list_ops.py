def append(list1, list2):
    list=[None]*(len(list1)+len(list2))
    start=0
    for value in list1:
            list[start]=value
            start+=1
    for value2 in list2:
        list[start]=value2
        start+=1
    return list
        


def concat(lists):
    concatlist=[]
    for eachlist in lists:
        concatlist=concatlist+eachlist
    return concatlist


def filter(function, list):
    predicated=[]
    for item in list:
        if function(item):
            predicated.append(item)
    return predicated


def length(list):
    count=0
    for item in list:
        count+=1
    return count 


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    result = initial
    for item in list:
        result = function(result, item)
    return result


def foldr(function, list, initial):
    result = initial
    for item in reverse(list):
        result = function(item, result)
    return result


def reverse(list):
    result = []
    for item in list:
        result.insert(0, item)
    return result
        
