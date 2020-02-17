import wget
import os

# NO listdlls
def listdlls():
    filename = wget.download('https://www.dropbox.com/s/by4ca7zwzcqyt12/Listdlls.exe?dl=1')
    os.rename(filename, u'' + os.getcwd() + '/' + filename)
