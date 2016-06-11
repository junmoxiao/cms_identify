import glob, os

file_list = []
for a in glob.glob('./cms/*'):
    file_list.append(a)


for f in file_list:
    os.system('mv f ' + './cms/' +f.split('/')[-1][:-1])
