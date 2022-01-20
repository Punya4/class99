import os
import shutil
#os.mkdir('/Users/OneDrive/Desktop/whjr/class99/NewFolder')
#path = '/usr/local/bin/'
#isExsist=os.path.exists(path)
#print(isExsist)
path ='/users/pankaj/onedrive/desktop/'
#route_ext=os.path.splitext(path)
#print('route part',route_ext[0])
#print('ext part',route_ext[1],'\n')
f=os.listdir(path)
source='/users/pankaj/onedrive/desktop/file.txt'
destination='/users/pankaj/onedrive/desktop/file_copy.txt'
dest=shutil.move(source,destination)
print(f)