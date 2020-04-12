import csv

def ReadCsv():
    csv_reader=csv.reader(open('class.csv',encoding='utf-8'))
    L=[]
    for row in csv_reader:
        L.append(row)
    return L

if __name__=='__main__':
    K=ReadCsv()
    print(K)
