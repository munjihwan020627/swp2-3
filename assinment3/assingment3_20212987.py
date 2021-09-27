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
                print("추가할 학생의 이름, 나이, 점수를 공백을 두고 입력하세요.")
        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except IndexError:
                print('삭제할 학생의 이름을 입력하세요.')
        elif parse[0] == 'show':
            try:
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey, 'All')
            except KeyError:
              print('show 뒤에는 정렬 기준을 입력하세요.')
        elif parse[0] == 'find':
            try:
                sortKey = 'Score'
                showScoreDB(scdb, sortKey, parse[1])
            except IndexError:
                print('find 뒤에는 찾고자 하는 학생의 이름을 입력하세요.')
        elif parse[0] == 'inc':
            try:
                addScore(scdb, parse[1], parse[2])
            except IndexError:
                print('inc 뒤에는 학생의 이름과 추가할 점수를 공백을 두고 입력하세요.')
            except ValueError:
                print('추가할 점수는 정수 형태로 입력해주세요.')
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
