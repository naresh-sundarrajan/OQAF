import pandas as pd
import csv
'''
with open("/Users/naresh/Documents/workspace/Environments/Test1/acc_dat.csv", "r") as f:

    reader = csv.reader(f)
    column_header = next(reader)
    header_len = len(column_header)
    count_negatives=0
    count_greaterthan130=0
    count_negatives=0
    for row in reader:
        #print(', '.join(row))
        count +=1
        print(row)

print (count)
'''

my_csv = pd.read_csv('/Users/naresh/Documents/workspace/Environments/Test1/acc_dat.csv')
column = my_csv.AGE
count_zero=0
count_greaterthan130=0
count_negatives=0
for row in column:
    if row == 0:
        count_zero += 1
    if row < 0:
        count_negatives +=1
    if row >= 130:
        count_greaterthan130 +=1

print(count_zero)
print(count_negatives)
print(count_greaterthan130)
count_tot = count_zero+count_negatives+count_greaterthan130
print("total:",count_tot)
    #print (row)
#inaccurate_values - inconsistencies:( negatives, 0, 130,150)
