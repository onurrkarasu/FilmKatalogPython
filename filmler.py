# Filmler katalogu Uygulamasi

filmler={
    "Kara Korsanın Laneti":{"Yapım Yılı":1957,"Imdb":8.2,"Tür":"Korku"},
    "Sineğin İntikamı":{"Yapım Yılı":2957,"Imdb":1.2,"Tür":"Belgesel"}
}

# Fonksiyon Örneği
def filmEkle():
    film_adi=input("Film adı girin :")
    global filmler  #Filmler değişkenini fonksiyon kullanmak için global anahtarını yazar ve izin isteriz.
    if film_adi:
        yapim_yili=input("Yapım yılını Girin : ")
        imdb=input("İmbdb puanını Girin : ")
        film_turu=input("Film Türünü girin : ")

        filmler[film_adi]={"Yapım Yılı":yapim_yili,"Imdb":imdb,"Tür":film_turu}
        print("Film başarıyla eklendi...")
    else:
        print("Film adı boş bırakılamaz...")



def filmSil():
    film_adi=input("Silinecek Filmin Adını girin :")
    global filmler
    if film_adi:
        filmler.pop(film_adi)
        print("Film başarıyla Silindi")
    else:
        print("Film adı geçersiz, Silme işlemi hatalı")



def filmGetir():
    aranan_film_adı=input("Aradığın Filmin Adını gir :")
    if aranan_film_adı in filmler.keys():
        film=filmler.get(aranan_film_adı)
        yapım_yılı=film.get("Yapım Yılı","Yapım yılı girilmemiş")
        imdb=film.get("Imdb","Imdb Girilmemiş")
        film_turu=film.get("Tür","Film Türü Girilmemiş")

        print("Film Adı :{}   Yapım Yılı : {}  Imdb : {}  Tür : {}  ".format(aranan_film_adı,yapım_yılı,imdb,film_turu) )
    else:
        print("Film adı eşleşmiyor, Böyle bir film yok.")
    input("Devam etmek için bir tuşa basın.")



def filmleriListele():
    for film in filmler:
        film_adi=film
        yapim_yili=filmler[film].get("Yapım Yılı","Yapım yılı girilmemiş")
        imdb=filmler[film].get("Imdb","Imdb Girilmemiş")
        film_turu=filmler[film].get("Tür","Tür Girilmemiş")
        print("Film Adı :{}   Yapım Yılı : {}  Imdb : {}  Tür : {}  ".format(film_adi, yapim_yili, imdb,
                                                                             film_turu))
        print("="*75)
    input("Devam etmek için bir tuşa basın.")


while True:
    print(""" 
        [1]   Tüm Filmleri Listele
        [2]   Film Ara
        [3]   Film Ekle
        [4]   Film Sil
        """)
    secenek=int(input("Seçiminizi yapınız ..."))
    if secenek==1:
        filmleriListele()
    elif secenek==2:
        filmGetir()
    elif secenek==3:
        filmEkle()
    elif secenek==4:
        filmSil()
    else:
        print("Herhangi bir seçim yapmadınız!!!")

