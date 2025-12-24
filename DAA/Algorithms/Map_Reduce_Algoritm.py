from multiprocessing import Pool
def mapper(chunk): 
    from collections import Counter
    return Counter(chunk.split())
def reducer(counters):
    from collections import Counter
    total=Counter()
    for c in counters: total.update(c)
    return total
if __name__=="__main__":
    text = "alpha beta alpha gamma beta alpha delta"
    chunks = [text[:20], text[20:]]  # simulate splits
    with Pool(2) as p:
        maps = p.map(mapper, chunks)
    print(dict(reducer(maps)))




