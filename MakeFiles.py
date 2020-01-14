import os
import subprocess
import time

os.chdir(r'.\Resources')
fileNames = os.listdir(os.getcwd())

for fileName in fileNames:
    file = open(fileName, 'a')
    file.write('\nimport shelve')
    file.write('\nshelfFile = shelve.open(\'' + fileName[0:-4] + '\')')
    file.write('\nshelfFile[\'A\'] = A')
    file.write('\nshelfFile[\'N0\'] = N0')
    file.write('\nshelfFile[\'N1\'] = N1')
    file.write('\nshelfFile[\'N2\'] = N2')
    file.write('\nshelfFile[\'P\'] = P')
    file.write('\nshelfFile[\'udzial\'] = udzial')
    file.write('\nshelfFile[\'doktorant\'] = doktorant')
    file.write('\nshelfFile[\'pracownik\'] = pracownik')
    file.write('\nshelfFile[\'czyN\'] = czyN')
    file.write('\nshelfFile[\'u\'] = u')
    file.write('\nshelfFile[\'w\'] = w')
    file.write('\nshelfFile[\'monografia\'] = monografia')
    file.write('\nshelfFile[\'authorIdList\'] = authorIdList')
    file.write('\nshelfFile[\'publicationIdList\'] = publicationIdList')
    file.write('\nshelfFile.close()')
    file.close()
    pre, ext = os.path.splitext(fileName)
    os.rename(fileName, pre + '.py')

fileNames = os.listdir(os.getcwd())
for fileName in fileNames:
    subprocess.Popen(['C:\\Users\\mateu\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe', fileName])






