satis=500
birim=20
ciro=5000
i=0
while True:
    satis=satis+200
    birim=birim+10
    ciro=ciro+(satis*birim)
    i=i+1
    if(ciro>500000):
        print(i/12,"yıl sonra 500.000TL den fazla ciro olur.")
        break
        
    
