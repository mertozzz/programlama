i=1
topdefurun=0
while 1:
    gunlukdefurun=int(input(("bugün kaç defolu ürün çıktı:")))

    topdefurun+=gunlukdefurun

    if(topdefurun>(200*i)):

        print("bugüne kadar ürettiğiniz defolu ürün oranı toplam üretiminizin %20 sinden daha fazla üretim yapamazsınız")
        break

    print(i,"gün boyunca toplam",
          (i*200),"adet ürün ürettiniz.Bunlardan",topdefurun,"adedi defoludur")

    if(gunlukdefurun>(200*20/100)):
        print("dikkat bugün ürettiğimiz defolu ürün sayısı çok fazladır.")
        break
    i+=1


            
