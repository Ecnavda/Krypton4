from sys import argv
from string import ascii_uppercase

def main(x):
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

    keyLen = input('Enter the length of the key: ')
    userKey = raw_input('Enter the key: ')
    storage = ''
    counter = 0
    keyCounter = 0

    with open(x,'r') as inFile:
        for i in inFile.read():
            if i in ascii_uppercase:
	        inConv = StoI[i]
                keyCounter = counter % keyLen
                outConv = inConv - StoI[userKey[keyCounter].upper()]
                if outConv < 0: outConv += 26
                storage += ItoS[str(outConv)]
                counter += 1
    print(storage)


if __name__ == '__main__':
    main(argv[1])
