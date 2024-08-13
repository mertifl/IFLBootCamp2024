# Kullanıcıdan alınan 2 tam sayı ile aritmetiksel işlemler yapan basit bir hesap makinesi uygulamasıdır.
# Birinci Sayıyı Giriniz: 5
# İkinci Sayıyı Giriniz: 4
# İşlemler
# --------
# 1. Toplama
# 2. Çıkarma
# 3. Çarpma
# 4. Bölme
# 5. Kuvvet Alma
# Yapmak İstediğiniz İşlemi Giriniz: 3
# 5 x 4 = 20
# Başka işlem yapmak ister misiniz? (e/h): h
# Hesap Makinesi Yazılımını kullandığınız için teşekkür ederiz.
# İFL Summer Boot Camp 2024
# import math Tüm matematik kütüphanesini çağırmak yerine sadece ilgili fonksiyonu/komutu/sabiti çağıralım!!!
from math import sqrt
devam='e'
while devam=='e':
    sayi1 = int(input("Birinci Sayıyı Giriniz:"))
    sayi2 = int(input("İkinci Sayıyı Giriniz:"))
    baslik = "İşlemler:"
    print(baslik)
    print("-"*len(baslik))
    print("1. Toplama","2. Çıkarma","3. Çarpma","4. Kalansız Bölme","5. Kuvvet Alma","6. Tam Bölme","7. Kalanı Bulma","8. Karekökünü hesaplama",sep="\n")
    islem = int(input("Yapmak İstediğiniz İşlemi Giriniz:"))
    if islem==1:
        print(sayi1,"+",sayi2,"=",sayi1+sayi2)
    elif islem==2:
        print(f"%d - %d = %d"%(sayi1,sayi2,sayi1-sayi2))
    elif islem==3:
        print(f"{sayi1} x {sayi2} = {sayi1*sayi2}")
    elif islem==4:
        if sayi2==0:
            print("Sıfıra bölme hatası!!!")
            break
        else:
            print(f"%d / %d = %.2f"%(sayi1,sayi2,sayi1/sayi2))
    elif islem==5:
        print(f"%d ^ %d = %d"%(sayi1,sayi2,sayi1**sayi2))
    elif islem==6:
        if sayi2==0:
            print("Sıfıra bölme hatası!!!")
            break
        else:
            print(f"%d // %d = %d"%(sayi1,sayi2,sayi1//sayi2))
    elif islem==7:
        print(sayi1,"MOD",sayi2,"=",sayi1%sayi2)
    elif islem==8:
        print(f"{sayi1} sayısının karekökü: {sqrt(sayi1)}")
        print(f"%d sayısının karekökü: %.2f"%(sayi2,sqrt(sayi2)))
    else:
        print("Hatalı işlem girilmiştir.")
    devam = input("Başka işlem yapmak ister misiniz? (e/h):").lower()
print("Hesap Makinesi Yazılımını kullandığınız için teşekkür ederiz.\nİFL Summer Boot Camp 2024")
