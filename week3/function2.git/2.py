

def imdb(dict):

    l = []

    for i in dict:

        if i["imdb"]>5.5:

            l.append(i["name"])

    return l

print(imdb(l))

