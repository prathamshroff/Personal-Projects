import csv
path = "/content/accounts.txt"

def conc_str(sentence):
    result = ""
    for word in sentence:
        result += str(word) + " "
    return result[:-1]

csv_arr = []
with open(path, "r") as file1:
    FileContent = file1.readline()
    i = 0
    for line in file1:
        lc_line = line.strip().split()
        if len(lc_line) >= 1:
          if len(lc_line[0]) >= 3:
            if lc_line[0][0].isnumeric() and (lc_line[0][1].isnumeric() or lc_line[0][2].isnumeric()):
              lc_line[2] = conc_str(lc_line[2:])
              lc_line = lc_line[:3]
              csv_arr += [lc_line]
              # print(lc_line)
    print(csv_arr)

with open("new_accounts.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(csv_arr)
