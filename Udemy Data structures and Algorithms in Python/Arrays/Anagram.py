#Anagram is when given two sentences have same set of alphabets like scar and cars

def anagram1(S1,S2):
    S1= (S1.replace(" ","")).lower()
    S2= (S2.replace(" ","")).lower()
    #str1=str1.replace("d","")
    return sorted(S1)==sorted(S2)



def anagram(S1, S2):
    S1=S1.replace(" ","").lower()
    S2=S2.replace(" ","").lower()
    # S1=list(S1)
    # S2 = list(S2)
    i=0
    if(len(S1)!=len(S2)):
        return False
    while i > len(S1):
        if(S1[i] in S2):
            i=i+1
        else:
            return False
    return True


print(anagram("qlint eastwood","old west action"))