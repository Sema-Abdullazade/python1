#1). Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
#Userden alinan 5 cavabi bir listde sirali seklinde yerlesdirin:
#[4,1,78,99,45] >> [1,4,45,78,99]
ededler=[]
for i in range(5):
    a=int(input("Ədədi daxil edin: "))
    ededler.append(a)
ededler.sort()
print(ededler)




#2). Daxil edilmiş cümlənin bütün sözlərini alfabetik düzülüşlü sözlərə çevirib nəticəni çap edin. Misal üçün ."sabahin xeyir". 
#Bu şəkildə olacaq  : "abhins exiry"    . Hər bir sözdəki hərflər alfabetik sırasına görə düzüldü. 

metn_herfleri=[]
a=input("Mətni daxil edin: ")
for i in a:
    metn_herfleri.append(i)
metn_herfleri.sort()
print(metn_herfleri)




#3.)Tutaq k, n=13. istifadəçi bu n ededini inputda  daxil edənə qədər input alın ve 13 daxil etdikdə desin ki, məsələn 5 cəhdə tapdız, yəni, neçə cəhdə 
#tapdığını print etsin. while istifade edin . Aşağıdakı inputlarlardakı dəyərlər sadəcə nümunədir. 
#ilk input== 4   
#ikinci input == 7
#ucuncu input == 2
#dorduncu input == 13

#tebrikler . 4 cehdde 13 reqemeni tapdiz
n = 13
say = 1
while True:
    a = int(input("Ədədi daxil edin: "))
    if a == n:
        print("Cəhdlərin sayı: ", say)
        break
    else: 
        say += 1






#4). 1 ile 100 arasinda sade ededleri print edin. (for loops)
eded1 = int(input("Ilk ededi daxil edin:"))
eded2 = int(input("Son ededi daxil edin:"))
def ededin_bolenleri(a):
    if a > 0:
        bolenler = [i for i in range(1, a+1) if a % i == 0]
    else:
        print("Bu ededin bolenlerin tapmaq mumkun deyil")
        return []
    return bolenler

def araliqdaki_sade_ededleri_tapan(a, b):
    sadeler = []
    for i in range(a+1, b):
        if len(ededin_bolenleri(i)) == 2:
            sadeler.append(i)
    return sadeler


print(araliqdaki_sade_ededleri_tapan(eded1, eded2))

