personel={"ahmet":28000,"mehmet":19500,"enes":55000,
"tuğçe":72000,"elif":41000,"tuba":19000,"şenay":12500,"metin":36000}
def zam_hesaplama(çalisanlar:dict):
    for my_key, my_value in personel.items():
        yeni_çalışanlar=[]
        if my_value>=0 and my_value<=20000:
            zamlı_maas=my_value+(my_value*(55/100))
        elif my_value>=20001 and my_value<=40000:
            zamlı_maas=my_value+(my_value*(40/100))
        elif my_value>=40001 and my_value<=60000:
            zamlı_maas=my_value+(my_value*(25/100))
        else:
            zamlı_maas=my_value+(my_value*(10/100))
        yeni_çalışanlar[my_key]=my_value*zamlı_maas
    return yeni_çalışanlar
personel.items()
        
