from sklearn.model_selection import train_test_split

file = open('data/train_traffic_2.raw','r')
list_name = []
for line in file:
    list_name.append(line.strip('\n'))
train_list, val_list = train_test_split(list_name, test_size = 0.1, shuffle = 44)

with open('data/train_traffic_2.txt','w') as f:
    for name in train_list:
        f.write(name + '\n')
with open('data/val_traffic_2.txt','w') as f:
    for name in val_list:
        f.write(name + '\n')