import csv,sys, operator, itertools

ids=[]

# #učitamo opt i z korigirani
opt_sup=[58,177,71,155,60,36,13,26]
z=[23, 15, 28, 64, 40, 15, 8, 12]
krvne_grupe=['0-', '0+', 'A-','A+', 'B-', 'B+', 'AB-', 'AB+']
koliko_fali_grupa=[]
for i in range(0, len(z)):
    koliko_fali_grupa.append(opt_sup[i]-z[i])
print(koliko_fali_grupa)

with open('ids.csv', newline='') as f:
  reader = csv.reader(f)
  for row in reader:
   ids=row
   break

print(len(ids))
print(ids)
potencijalni=[]
kandidati=[]
cnt=0
with open('NewFile.csv', newline='') as csvfile:
#with open('donors.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['id']in ids:
            if ((int(row['last_donation']) >= 90 and row['sex'] == 'M') or ((int(row['last_donation']) >= 120 and row['sex'] == 'Z'))):
                potencijalni.append(row)
    print(potencijalni)
    print(len(potencijalni))
    cnt=len(ids)-len(potencijalni)
    print(cnt)
    for p in potencijalni:
        if koliko_fali_grupa[krvne_grupe.index(p['blood_group'])] > 0:
            if float(p['frequency']) > 1:
                print(koliko_fali_grupa[krvne_grupe.index(p['blood_group'])])
                kandidati.append(p['id'])


with open('ids_candidate.csv', 'w') as f:
    #writer = csv.writer(f)
    for index, kandidat in enumerate(kandidati):
        f.write(kandidat)
        if index < len(kandidati)-1:
            f.write(',')

