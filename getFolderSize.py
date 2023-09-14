# This file will prin all folders where size >1MB
import os
# Change directory
b_to_mb = 1048576
target_dir = 'C:\\My Documents\\'
os.chdir(target_dir)
# Print your working directory
print('Current Working Directory: {0}\n'.format(os.getcwd()))

#iterate over directories
for path, dirs, files in os.walk(os.getcwd()):
    size=0
    for f in files:
        fp=os.path.join(path,f)
        size+=os.path.getsize(fp)
        mb = size/b_to_mb
    # print size of directory
    if mb>1:
        print('{0} {1}. \nSize: {2}MB'.format(path,dirs,mb))
