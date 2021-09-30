import pickle

dbfilename = 'test3_4.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':

            if type(parse[2]) == int or type(parse[3]) == int:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            else:
                print('다시입력해주세요')
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
                        break
            except IndexError:
                print("index error")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'find':
            lst =[]
            for a in scdb:
                if a['Name'] == parse[1]:
                    lst.append(a)
            showScoreDB(lst, 'Name')
        elif parse[0] == 'inc':
            try:
                for a in scdb:
                    if a['Name'] == parse[1]:
                        a['Score'] = str(int(parse[2]) + int(a['Score']))
            except ValueError:
                print("Value error")
        elif parse[0] == 'del':
            for a in scdb:
                if 'name' == parse[1]:
                    scdb.remove(a)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)

