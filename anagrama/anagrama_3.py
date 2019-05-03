def strtodict(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i]  = 1
    return dict

def isAnagram(p1, p2):
    
    if len(p1) != len(p2):
        return False
    
    result = []
    dictp1 = strtodict(p1)
    dictp2 = strtodict(p2)
    for key, value in dictp2.items():
        if key in dictp1 and dictp1[key] == value:
            result.append(True)
    return len(result) == len(dictp1)
    
            
print(isAnagram('amor', 'roma'))    
print(isAnagram('amor', 'rama'))            
print(isAnagram('amor', 'casa'))            
print(isAnagram('amar', 'rama'))
print(isAnagram('riesgo', 'sergio'))