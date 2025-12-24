def kmp(text, pattern):
    lps=[0]*len(pattern)
    j=0
    for i in range(1,len(pattern)):
        while j>0 and pattern[i]!=pattern[j]: j=lps[j-1]
        if pattern[i]==pattern[j]: j+=1; lps[i]=j
    i=j=0; res=[]
    while i<len(text):
        if text[i]==pattern[j]: i+=1; j+=1
        if j==len(pattern): res.append(i-j); j=lps[j-1]
        elif i<len(text) and text[i]!=pattern[j] and j>0: j=lps[j-1]
        elif i<len(text) and text[i]!=pattern[j]: i+=1
    return res
print(kmp("ABABDABACDABABCABAB","ABAB"))
