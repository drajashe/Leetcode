"""Represent a string of the form AAaaaaaBBBBB as A2a5B5""""""RUNLENGTH COMPRESSION ALGORITHM"""def compress(string1):    com=str()    #string1=list(string1)    #print(string1)    count=1    l=i=1    length=len(string1)    if(length==0):        return ""    elif(length==1):        return (string1+str(1))    while i < length:        if(string1[i]==string1[i-1]):            count+=1        else:            com=com+string1[i-1]+str(count)            count=1        i=i+1    com=com+string1[i-1]+str(count)    #count=0    #print com    return comcompress('B')