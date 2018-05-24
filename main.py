import csv,sys, operator


min_sup=[38,115,46,100,38,23,8,16]
max_sup=[78,240,96,210,82,50,18,36]
p=[35,105,42,91,35,21,7,14]


opt_sup=[58,177,71,155,60,36,13,26]
z=[60,120,69,154,80,31,17,24]

nula_minus=0
nula_plus=0
A_minus=0
A_plus=0
B_minus=0
B_plus=0
AB_minus=0
AB_plus=0
r=[]
new=[]


def loss(x, min, max, r):
    if x<=min:
        return (200/r)*(min-x)+35
    elif min < x <= (r/3)+min:
        return (100/r)*(min+(r/3)-x)
    elif (r/3)+min < x <= (2*r/3) + min:
        return 0
    elif (2*r/3)+ min < x <= max:
        return (100/r)*(x-(2*r/3) -min)
    elif x>max:
        (200/r)*(x-max)+35

#sort po frekvenciji
data = csv.reader(open('donors.csv'),delimiter=',')
sortedlist = sorted(data, key=operator.itemgetter(1), reverse=True)

with open("NewFile.csv", "w") as f:
          fileWriter = csv.writer(f, delimiter=',')
          for row in sortedlist:
              fileWriter.writerow(row)



with open('NewFile.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
# trebamo znati koliko koje krve grupe ima donatora
    for row in reader:
      if((int(row['last_donation'])>=90 and row['sex']=='M') or ((int(row['last_donation']) >=120 and row['sex'] == 'Z'))):
          if(row['blood_group']=='0-'):
              nula_minus=nula_minus+1
          elif(row['blood_group']=='0+'):
              nula_plus=nula_plus+1
          elif(row['blood_group']=='A-'):
              A_minus=A_minus+1
          elif(row['blood_group']=='A+'):
              A_plus=A_plus+1
          elif(row['blood_group']=='B-'):
              B_minus=B_minus+1
          elif(row['blood_group']=='B+'):
              B_plus=B_plus+1
          elif(row['blood_group'] == 'AB-'):
              AB_minus = AB_minus + 1
          elif (row['blood_group'] == 'AB+'):
              AB_plus= AB_plus + 1
    # print(nula_minus,nula_plus,A_minus,A_plus,B_minus,B_plus,AB_minus,AB_plus)


    for i in range(0,len(min_sup)):
      r.append(max_sup[i]-min_sup[i])
      print(r[i])


for i in range(0,len(z)):
    if(z[i]>max_sup[i] or z[i]<min_sup[i]):
        print('Nije moguća korekcija')
        break

# obrnimo vektore od AB+, do 0-
min_rev=list(reversed(min_sup))
opt_rev=list(reversed(opt_sup))
z_rev= list(reversed(z))
razlika1=0
new_z=reversed(z)
opt_rev1=list((opt_rev))
for i in range(len(z_rev)):
    if z_rev[i] < opt_rev[i]:
        razlika1=opt_rev[i]-z_rev[i]
        for j in range(i, len(z_rev)):
            if z_rev[j] > opt_rev[j]:
              razlika2=z_rev[j]-opt_rev[j]
              if razlika1<=razlika2:
                  z_rev[i]+=razlika1
                  z_rev[j]-=razlika1
                  break;
              elif razlika1>razlika2:
                  z_rev[i] += razlika2
                  z_rev[j] -= razlika2
z=list(reversed(z_rev))
print(z)

for i in range(0, len(z)):
    z[i]-=p[i]
print(z)

suma=0

for i in range(0, len(z)):
    gubitak=int(loss(z[i], min_sup[i], max_sup[i], r[i]))
    suma+=gubitak
    print(suma)

with open('ids.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)

    # with open('donors.csv', newline='') as csvfile:
    #     reader = csv.DictReader(csvfile)
    # for row in reader:
    #     if row['id']






