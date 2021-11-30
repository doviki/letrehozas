# Tölts fel egy tömböt véletlen számokkal 0-100 értékekkel 10 darabot!
import random
sorsoltSzamok=[]
for x in range(10):
    vszam=random.randint(1,10)
    sorsoltSzamok.append(vszam)
print (sorsoltSzamok)
# Írd ki a számok átlagát!
print("Átlag: ")
atlag=sum(sorsoltSzamok)/len(sorsoltSzamok)
print(atlag)

# Van-e benne páros szám? eldöntés tétele
vane=False;
for x in sorsoltSzamok:
    if(x%2==0):
        vane=True
        break

if (vane==True):
    print("Van a listában páros szám!")
else:
    print("Nincs a listában páros szám!")
# Add össze az 50-nél nagyobbakat!
#feltételes összegzés
osszeg=0
for x in sorsoltSzamok:
    if x>50:
        #osszeg=osszeg+x
        osszeg+=x
print("Az 50-nél nagyobb számok összege: ",osszeg)

# Számold meg hány 9-es van benne!
db=0
for j in sorsoltSzamok:
    if j==9:
        db+=1
print("A tömbben {} db '9'-es van.".format(db))   