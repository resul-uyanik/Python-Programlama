def sinav_notu(liste_vize:list,liste_final:list):
    sonuc_listesi=[]

    for sayi in range(len(liste_vize)):
        vize_notu=liste_vize[sayi]
        final_notu=liste_final[sayi]

        son_not=(vize_notu*0.4) + (final_notu*0.6)
        if(son_not>=50):
            sonuc_listesi.append(son_not)
    return sonuc_listesi 
vize_notlari=[55,87,12,23,96]
final_notlari=[28,39,58,85,77]

sinav_sonuclari=sinav_notu(vize_notlari,final_notlari)

print(f"sınav sonuçlari aşağıdaki gibidir: ")
print(sinav_sonuclari)