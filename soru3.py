girilen=''
toplam=0
while(girilen!=0):
    girilen=int(input("Bir sayı giriniz:"))
    toplam += (girilen%3)
print("kalanların toplamı:",toplam)
