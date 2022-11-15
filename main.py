from tokenize import String

from sklearn import preprocessing

from ACDTW import *


beef_data = np.loadtxt(r'C:\Users\86182\Desktop\Beef\Beef_TRAIN.txt')
x = beef_data[0][1:]
y = beef_data[1][1:]
result_list = []
label_list = []
length = beef_data.shape[0]-20
for i in range(length):
    for j in range(length):
        if i > j:
            x = beef_data[i][1:].reshape(-1,1)
            y = beef_data[j][1:].reshape(-1,1)
            x_label = beef_data[i][0]
            y_label = beef_data[j][0]
            label = str(x_label)+'_' + '%s' %(i) + '--' + str(y_label)+'_'+'%d' %(j)
            x = preprocessing.MaxAbsScaler().fit_transform(x)
            y = preprocessing.MaxAbsScaler().fit_transform(y)
            result, C, D1, path = acdtw(x, y)
            result_list.append(result)
            label_list.append(label)

print(result_list)
print(label_list)