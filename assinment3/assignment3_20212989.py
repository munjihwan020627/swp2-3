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
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except IndexError:
                print("IndexError")
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey, 'All')
            except KeyError:
              print("KeyError")
        elif parse[0] == 'find':
            try:
                sortKey = 'Score'
                showScoreDB(scdb, sortKey, parse[1])
            except IndexError:
                print('IndexError')
        elif parse[0] == 'inc':
            try:
                addScore(scdb, parse[1], parse[2])
            except IndexError:
                print('IndexError')
            except ValueError:
                print('ValueError')
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print("IndexError")
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname, findName):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            if (findName == 'All') or (p['Name'] == findName):
                print(attr + "=" + p[attr], end=' ')
        if (findName == 'All') or (p['Name'] == findName):
            print()

def addScore(scdb, Name, amount):
    for p in scdb:
      if Name == p['Name']:
        p['Score'] = int(p['Score']) + int(amount)
        p['Score'] = str(p['Score'])


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
