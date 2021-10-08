import os
from posix import listdir
import shutil
import time

path = input("path to the location to remove old files")
days = input("delete files before last")

tc=(time.time())-1-1*86400


for filename in os.listdir((path)):
    if os.path.getmtime(os.path.join(path,filename))<tc:
        if os.path.isfile(os.path.join(path,filename)):
            print(filename)
            os.remove(os.path.join(path.filename))
        elif os.path.isdir(os.path.join(path,filename)):
            print(filename)
            shutil.rmtree((os.path.join(path,filename)))
            


