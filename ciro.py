def katmadeğerciro():
    x=int(input("Topla satış:"))
    a=int(input("Hammadde maliyeti giriniz:"))
    b=int(input("Bakım Onarım Giderleri giriniz:"))
    c=int(input("Sevkiyat Giderleri giriniz:"))
    d=int(input("Satın Alınan Hizmet Giderleri giriniz:"))
    topsatis=x
    topmaliyet=(a+b+c+d)
    ciro=(topsatis-topmaliyet)
    if ((ciro)>1000):
        print("İşletme katma değer cirosu yüksek")
    elif (ciro>=500) and (ciro<=999):
        print("işletme katma değer cirosu normal")
    else:
        print("işletme katma değer cirosu düşük")
    
