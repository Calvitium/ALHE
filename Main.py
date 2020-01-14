import os
import shelve
import TokenClass
import pprint


def fillDiscipline(shelf):
    global disciplinesTokens
    tokens = []
    file = shelve.open(shelf)
    A = file['A']
    P = file['P']
    u = file['u']
    w = file['w']
    udzial = file['udzial']
    publicationIds = file['publicationIdList']
    authorIds = file['authorIdList']
    for i in range(A):
        if file['pracownik'][i] != 1:
            continue
        for j in range(P):
            if u[i][j] != 0:
                tokens.append(TokenClass.Token(authorIds[i],
                                               publicationIds[j],
                                               u[i][j],
                                               udzial[i],
                                               w[i][j]))
    disciplinesTokens[shelf] = tokens
    file.close()


#############################
#         MAIN  CODE        #
#############################
os.chdir(r'.\Resources')

shelvesNames = []
disciplinesTokens = {}

for fileName in os.listdir(os.getcwd()):
    if fileName.endswith(".dat"):
        shelvesNames.append(fileName[0:-4])


for shelf in shelvesNames:
    fillDiscipline(shelf)


