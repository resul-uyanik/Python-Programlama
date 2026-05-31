ogrenciler={"Furkan":[85,56],"Ahmet":[52,38],"Mehmet":[28,83],
"Tuğçe":[76,13],"Tuba":[25,37],"Aslı":[75,85],"Murat":[63,72]}
def not_hesaplama(gecici_dict:dict):
    for my_key, my_value in ogrenciler.items():
        bos_liste=[]
        vize_notu=ogrenciler.items[1][0]
        final_notu=ogrenciler.items[1][1]
        not_hesapla= (vize_notu*0.4)+(final_notu*0.6)
        if not_hesapla>=50:
            bos_liste.append(f"{my_key} {not_hesapla} ile geçti")
        else:
            bos_liste.append(f"{my_key} {not_hesapla} ile kaldı")
    return bos_liste
ogrenciler.items()
        
