def flatten(iterable):
    new_list=[]
    for item in iterable:
        type_of=type(item)
        if type_of is list or type_of is tuple:
            new_list += flatten(list(item))
        else:
             if item is not None:
                new_list.append(item)
    return new_list

