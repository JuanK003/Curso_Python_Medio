import csv

def read_csv(path):
   # Tu código aquí 👇
   with open(path,  'r') as csvfile:
    total = sum(int(i[1]) for i in csv.reader(csvfile))
   return total

response = read_csv('./data.csv')
print(response)