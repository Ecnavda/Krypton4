from sys import argv
from collections import Counter

def main(x, y):
   
    StoI = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4,
            'F':5, 'G':6, 'H':7, 'I':8, 'J':9,
            'K':10,'L':11,'M':12,'N':13,'O':14,
            'P':15,'Q':16,'R':17,'S':18,'T':19,
            'U':20,'V':21,'W':22,'X':23,'Y':24,
            'Z':25}

    ItoS = {'0':'A','1':'B','2':'C','3':'D','4':'E',
            '5':'F','6':'G','7':'H','8':'I','9':'J',
            '10':'K','11':'L','12':'M','13':'N','14':'O',
            '15':'P','16':'Q','17':'R','18':'S','19':'T',
            '20':'U','21':'V','22':'W','23':'X','24':'Y',
            '25':'Z'}

    counter = 0
    storage = []

    try:
        with open(x, 'r') as inFile:
            for i in inFile.read():
                if i == ' ':
                    pass
                elif i == '\n':
                    pass
                else:
                    result = counter % 6 # 6 is used because we are told it is
                                         # the keylength
                    if result == int(y):
                        storage.append(i)
                    counter += 1
    except Exception as e:
        print(e)
    finally:
        counter = 0
        magicNum = 0
        for x in Counter(storage).most_common():
            if counter == 0:
                magicNum = StoI[x[0]] - StoI['E']
                if magicNum > 25:
                    magicNum -= 26
                elif magicNum < 0:
                    magicNum += 26
                print('The most occurring letter will be used as "E"')
                print(str(magicNum) + ' ' + ItoS[str(magicNum)])
                counter += 1
            conv = StoI[x[0]] - magicNum
            if conv < 0:
                conv += 26
            print('Times: ' + str(x[1]) + ' Char: ' + x[0] + ' Num: ' + str(StoI[x[0]]) + ' Conv: ' + \
                  ItoS[str(conv)])

if __name__ == "__main__":
    main(argv[1], argv[2]) #First arg is filename, Second is used as key index
