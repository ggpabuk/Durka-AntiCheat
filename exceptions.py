import wget
import os


# Listdlls not found
def listdlls():
    link = 'https://www.dropbox.com/s/by4ca7zwzcqyt12/Listdlls.exe?dl=1'
    filename = wget.download(link)
    os.rename(filename, u'' + os.getcwd() + '/' + filename)

    print('\n\n')
