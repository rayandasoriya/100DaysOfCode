from collections import Counter
def op(s1,s2):
    dict1 = Counter(s1)
    dict2 = Counter(s2)
    
    keys1 = dict1.keys()
    keys2 = dict2.keys()
    
    ComE = len(set(keys1).intersection(keys2))
    
    if ComE == 0:
        return len(keys1)+len(keys2)
    else:
        return max(len(keys1),len(keys2)) - ComE

s1 = "bcadeh"
s2 = "hea"
print op(s1,s2) 
