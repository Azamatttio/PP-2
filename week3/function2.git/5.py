def ImC(Cat):

    l = []

    for i,e in enumerate(l):

        if Cat in e.values():

            l.append(e['imdb'])

    return sum(l)/len(l)




print(ImC("Romance"))
