# takes the file flag and stores it in a nested zip

import os
from random import random
from zipfile import ZipFile
import tarfile


ZipFile('thatsdeep.zip', mode='w').write("flag")

precedent = 'thatsdeep.zip'
for i in range(1, 666):
    if random() < 0.5:
        ZipFile('thatsdeep_current.zip', mode='a').write(precedent)
        os.rename('thatsdeep_current.zip', 'thatsdeep.zip')
        precedent = 'thatsdeep.zip'

        if os.path.isfile('thatsdeep.tar.gz'):
            os.remove('thatsdeep.tar.gz')
    else:
        tar = tarfile.open("thatsdeep_current.tar.gz", "w:gz")
        tar.add(precedent)
        tar.close()
        os.rename('thatsdeep_current.tar.gz', 'thatsdeep.tar.gz')
        precedent = 'thatsdeep.tar.gz'
        
        if os.path.isfile('thatsdeep.zip'):
            os.remove('thatsdeep.zip')
