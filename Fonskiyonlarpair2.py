# ucuncugunworkshop():
def enbuyuksayi():
    liste =[]
    for n in range(0,9):
        sayi = int(input('Sayı Giriniz: '))
        liste.append(sayi)
 
        n_buyuk = max(liste)
        print("Liste İçindeki En Büyük Sayı :", n_buyuk )
enbuyuksayi()

#

def ciftsayi():
    x = int(input("Bir üst limit değeri giriniz: "))

    for v in range(0, x+2 ,2):
        print(v)

    #3.kısım

    a = int(input("Bir üst limit değeri giriniz: "))
    y = int(input("Bir alt limit değeri giriniz: "))

    for i in range(y, a):
        if i%2 == 0:
            print(i)

ciftsayi()

#

#ucuncugunpaircalismasi

def fibonacci():
    FibonacciSeri = [1,1]
    a= int(input("Bir değer giriniz: ")) 
    while len(FibonacciSeri) < a:  
        sıradakiSayi = FibonacciSeri[-1] + FibonacciSeri[-2]  
        FibonacciSeri.append(sıradakiSayi)  
        print("Fibonacci:",FibonacciSeri)
fibonacci()

#

#mukemmelsayihesaplama

def mukemmelsayi():
    sayi = int(input("Bir sayı giriniz: "))  
    bolenler = []  

    for i in range(1, sayi):  
        if sayi % i == 0:  
            bolenler.append(i)  

    if sum(bolenler) == sayi:  
        print(sayi, "mükemmel bir sayıdır.")
    else:
        print(sayi, "mükemmel bir sayı değildir.")

mukemmelsayi()



