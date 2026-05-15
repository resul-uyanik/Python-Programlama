deger=int(input("Bir Değer Giriniz: "))
flag=False

if deger==0 or deger==1 or deger<0:
    print("Sayı asal değildir.")
elif deger>1:
    for i in range(2,deger):
        if deger%i==0:
            flag=True
            break
    if flag:
        print(f"{deger} değeri asal bir sayı değildir.")
    else:
        print(f"{deger} değeri asal bir sayıdır.")