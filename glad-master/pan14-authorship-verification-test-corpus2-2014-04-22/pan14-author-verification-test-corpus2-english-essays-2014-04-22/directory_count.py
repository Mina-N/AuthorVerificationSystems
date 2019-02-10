import os
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re

rootDir = '.'
filename = 'directory_info.txt'
directory_list = []
file_list = []
f = open(filename, "a")
#i = 0
for dirName, subdirList, fileList in os.walk(rootDir):
    f.write('Found directory: %s \n' % dirName)
    #i += 1
    #if (i % 5 == 0):
    if (dirName != "."):
        dirNameNew = re.sub('./EE', '', dirName)
        directory_list.append(int(dirNameNew))
        num_files = 0
        for fname in fileList:
            num_files += 1
        f.write(str(num_files) + '\n')
        file_list.append(num_files)
f.close()

#plt.tick_params(axis='both', which='major', labelsize=6)
#y_pos = np.arange(len(directory_list))
#num_files = file_list
#plt.bar(y_pos, num_files, align='center', alpha=0.5)
#plt.xticks(y_pos, directory_list)
#pd.plot(kind='scatter', x=directory_list, y=file_list, style=['o', 'rx'], s=12)
marker_size = 10
plt.scatter(directory_list, file_list, marker_size)
plt.ylabel('Text Samples')
plt.xlabel('Author')
plt.title('Text Samples Per Author in PAN 2014 Test Dataset English Essays')
plt.show()
#plt.savefig('PAN2014Test_TextSampleDistribution.jpeg')
