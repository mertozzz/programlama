def performans():
    x=int(input('standart çevrim giriniz:'))
    y=int(input('üretim miktarı:'))
    z=int(input('planlanmış üretim süresi:'))
    e=int(input('plansız duruş:'))
    performansH=((x*y)/(z-e))
    print (performansH)

def kullan():
    x=int(input('planlanmış üretim süresi:'))
    y=int(input('Plansız Duruş:'))
    z=int(input('Planlanmış Üretim Süresi :'))
    kulH=((x-y)/z)
    print (kulH)

def kalite():
    x=int(input('Sağlam Ürün Miktarı:'))
    y=int(input('Toplam Üretim Mitarı:'))
    kaliteH=x/y
    return kaliteH
def oee():
    x=int(input('Kullanılabilirlik :'))
    y=int(input('Performans:'))
    z=int(input('kalite:'))
    oeeH=x*y*z
    print (oeeH)
    


    

            
