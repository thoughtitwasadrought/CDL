import os, os.path, sys
from threading import Thread
NO_OF_CHARS = 256
path = "input/"

def badCharHeuristic(string, size):
    badChar = [-1]*NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i;
    return badChar

def search(txt, pat):
    m = len(pat)
    n = len(txt)
    badChar = badCharHeuristic(pat, m)
    s = 0
    while(s <= n-m):
        j = m-1
        while j>=0 and pat[j] == txt[s+j]:
            j -= 1
        if j<0:
            return 1
            s += (m-badChar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badChar[ord(txt[s+j])])
    return 0

def getFiles():
    filesList = []
    for f in os.listdir(path):
        filesList.append(f)
    return filesList

def searchFile(fileName, word):
    fp = open(path+fileName, 'r')
    line = fp.readline()
    while line:
        result=search(line.lower(), word.lower())
        if result == 1:
            fp.close()
            return 1
        line = fp.readline()
    fp.close()
    return 0

def parseToken(token, fileNames):
    if '(' in token:
        if '!' in token:
            # the lambda function flips the 0 and 1 values in the list
            return list(map(lambda x: 1-x,parseToken(token[2:-1],fileNames)))
        else:
            return parseToken(token[1:-1],fileNames)
    else:
        if "||" in token:
            terms = token.split("||")
            # the join uses || to reconstruct the string without the first term
            return list(map(lambda x,y: x or y,parseToken(terms[0],fileNames),parseToken("||".join(terms[1:]),fileNames)))
        else:
            query = [0] * len(fileNames)
            for i in range(0,len(fileNames)):
                query[i]=searchFile(fileNames[i],token)
            return query

def searchThreadFunction(files,tokens):
    results = [1] * len(files)
    for token in tokens:
        results = list(map(lambda x,y: x and y, results, parseToken(token.replace(" ",""),files)))
    for i in range(len(files)):
        if results[i] == 1:
            print(files[i])

def main():
    files=getFiles()
    query = sys.stdin.readline().rstrip()
    tokens = query.split("&&")
    print("Files that match the query:")
    threadList = []
    numThreads = 3
    for i in range(numThreads):
        start=int(i*len(files)/numThreads)
        if i == 3:
            end=len(files)-1
        else:
            end=int((i+1)*len(files)/numThreads)
        newThread = Thread(target = searchThreadFunction, args = (files[start:end],tokens))
        threadList.append(newThread)
    for thread in threadList:
        thread.start()
    for thread in threadList:
        thread.join()
if __name__ == '__main__':
    main()
