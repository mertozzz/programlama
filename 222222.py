def gelirHesapla():
    x=int(input("finansmanGelir giriniz:"))
    y=int(input("pazarGelir giriniz:"))
    z=int(input("kiraGelir giriniz:"))
    gelir=(x+y+z)
    return gelir
def giderHesapla():
    a=int(input("ucret giriniz:"))
    b=int(input("finansmanGider giriniz:"))
    c=int(input("pazarGider giriniz:"))
    d=int(input("kiraGider giriniz:"))
    e=int(input("muhasebeGider giriniz:"))
    gider=(a+b+c+d+e)
    return gider
def kar():
    x=int(input("finansmanGelir giriniz:"))
    y=int(input("pazarGelir giriniz:"))
    z=int(input("kiraGelir giriniz:"))
    a=int(input("ucret giriniz:"))
    b=int(input("finansmanGider giriniz:"))
    c=int(input("pazarGider giriniz:"))
    d=int(input("kiraGider giriniz:"))
    e=int(input("muhasebeGider giriniz:"))
    topgelir=(x+y+z)
    topgider=(a+b+c+d+e)
    karH=(topgelir-topgider)
    return karH
def kar1():
    x=int(input("finansmanGelir giriniz:"))
    y=int(input("pazarGelir giriniz:"))
    z=int(input("kiraGelir giriniz:"))
    a=int(input("ucret giriniz:"))
    b=int(input("finansmanGider giriniz:"))
    c=int(input("pazarGider giriniz:"))
    d=int(input("kiraGider giriniz:"))
    e=int(input("muhasebeGider giriniz:"))
    topgelir=(x+y+z)
    topgider=(a+b+c+d+e)
    karH=(topgelir-topgider)
    if ((topgelir-topgider)>1000):
                      print("karlıdır")
    
