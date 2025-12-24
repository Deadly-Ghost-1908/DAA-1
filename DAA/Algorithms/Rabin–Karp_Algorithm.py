def rabin_karp(text, pattern,d=256,q=101):
    m,n=len(pattern),len(text);h=p=t=0;res=[]
    for i in range(m): p=(d*p+ord(pattern[i]))%q; t=(d*t+ord(text[i]))%q
    for i in range(n-m+1):
        if p==t and text[i:i+m]==pattern: res.append(i)
        if i<n-m: t=(d*(t-ord(text[i])*pow(d,m-1,q))+ord(text[i+m]))%q
    return res
print(rabin_karp("GEEKS FOR GEEKS","GEEK"))



