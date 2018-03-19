def stok():
    koltuksayısı=int(input("koltuksay giriniz:"))
    x=koltuksayısı
    yataksayısı=int(input("yataksaygiriniz:"))
    y=yataksayısı
    dolapsayısı=int(input('dolapsayısınıgiriniz:'))
    z=dolapsayısı
    dönembaşıstok=print("dönembaşısto:",x,y,z)
    satılankoltuk=int(input("satılankoltuk:"))
    a=satılankoltuk
    satılanyatak=int(input("satılanyatak:"))
    b=satılanyatak
    satılandolap=int(input("satılandolap:"))
    c=satılandolap
    alınankoltuk=int(input("alınankoltuk:"))
    d=alınankoltuk
    alınanyatak=int(input("alınanyatak:"))
    e=alınanyatak
    alınandolap=int(input("alınandolap:"))
    f=alınandolap
    dönemsonustok=(x-a+d),(y-b+e),(z-c+f)
    print(dönemsonustok)
    ortalamastok=((x+(x-a+d))/2),((y+(y-b+e))/2),((z+(z-c+f))/2)
    print("ortalamastok:",ortalamastok)


    

    
    
    
    
