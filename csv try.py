import csv
name='vanshika'
with open("Book1.csv","r") as f2:
    cr=csv.reader(f2)
    for row in cr :
        for i in row:
            if i==name:
                print(i)
        #if row[0]==name:
        #print(row[1])
        #else:
         #   print("***Sorry, you have no previous records.***")
f2.close()
'''import csv
f=open("Book1.csv","a")
writer = csv.writer(f)
writer.writerow("ghi,jkl,mnop")
f.close()
'''
