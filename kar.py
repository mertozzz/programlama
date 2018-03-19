def ilkkar():
    x=int(input('yazılım geliri:'))
    y=int(input('finansman geliri:'))
    z=int(input('ürün satış:'))
    a=int(input('çalışan maaşları:'))
    b=int(input('kira gideri:'))
    c=int(input('donanım maliyetleri:'))
    ilkgelir=(x+y+z)
    ilkgider=(a+b+c)
    ilk6kar=ilkgelir-ilkgider
    return ilk6kar
def sonkar():
    k=int(input('yazılım geliri:'))
    l=int(input('finansman geliri:'))
    m=int(input('ürün satış:'))
    n=int(input('e-ticaret:'))
    d=int(input('çalışan maaşları:'))
    e=int(input('kira gideri:'))
    f=int(input('donanım maliyetleri:'))
    songelir=(k+l+m+n)
    songider=(d+e+f)
    son6kar=songelir-songider
    return son6kar
def karfarkı():
    i=ilkkar()
    s=sonkar()
    fark=(i-s)
    if ((fark)>5000):
        print("İşletme çok karlı")
    elif (fark>=1000) and (ciro<=5000):
        print("işletme karı normal")
    else:
        print("işletme yeterimce karlı değil")
        
    
          
