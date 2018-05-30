def count_score(word):
    return len(word)+2*(word.count('j')+word.count('k')+word.count('x')+word.count('z'))+(word.count('q')+word.count('f')+word.count('h')+word.count('l')+word.count('m')+word.count('p')+word.count('c')+word.count('v')+word.count('w')+word.count('y'))
def all_word(sort_word):
    store=[]
    for w in sort_word:
        for num in range(len(store)):
            store.append(store[num]+w)
        store.append(w)
    return store
def long_search(word):
    sort_word=sorted(word.lower())
    all=all_word(sort_word)
    dict={}
    yfile = open('dict.txt','r')
    line = yfile.readline()
    for i in line:
        data=(line.replace('\n','')).lower()
        dict[data]=''.join(sorted(data))
        line = yfile.readline()
    yfile.close()
    store=[]
    max=0
    max_word=""
    for num in range(len(all)):
        print (all[num])
        for v,t in dict.items():
            print(v)
            if t in all[num]:
                store.append(v)
                if max<count_score(t):
                    max=count_score(t)
                    max_word=v
    return store
