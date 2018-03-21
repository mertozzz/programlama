i=1
aylikodeme=0

while(i<=50):
    j=i
    aylikcalisilansüre=0

    while(j<=4):
        soru=i,".çalışan",j,".hafta kaç saat mesai yaptı?"
        haftalikcalisilansüre=int(input(soru))
        aylikcalisilansüre+=haftalikcalisilansüre


        j+=1

        if(aylikcalisilansüre>22):

            print("bir personel ayda 22 saatten fazla çalışmaz")
            aylikcalisilansüre-=haftalikcalisilansüre
    personelaylikmesai=((90*30)+(aylikcalisilansüre+(90*10/100)))
    print("",i,".çalışan bu ay",personelaylikmesai,"tl maaş alacaktır")

    aylikodeme+=personelaylikmesai

    i+=1

print("işletme bu ay bütün personellere toplam",personelaylikmesai,"tl ödeme yapacaktır")
    
