def mergeDic(d1, d2):
    d3 = {}
    
    for key,value in d1.items():
        d3[key] = value
        
    for key,value in d2.items():
        if key not in d3.keys():
            d3[key] = value
        
    return d3