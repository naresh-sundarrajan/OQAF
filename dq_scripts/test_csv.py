import csv
with open("/Users/naresh/Documents/workspace/Environments/Test1/acc_dat.csv", "r") as f:
    reader = csv.reader(f)
    column_header = next(reader)
    header_len = len(column_header)
for i in range(header_len):
    print (column_header[i])
