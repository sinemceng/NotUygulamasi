import datetime
dosyaAdi="notlar.txt"
notlar=[]

#strip() ile satırın başındaki ve sonundaki boşluk, tab veya yeni satır karakterlerini temizliyorsun.

def notlariYukle():
    try:
        with open(dosyaAdi, "r", encoding="utf-8") as dosya:
            for satir in dosya:
                satir = satir.strip()
                if not satir:
                    continue
                # Dosyada "tarih|konu|icerik" formatında saklıyoruz
                parts = satir.split("|", 2)
                if len(parts) == 3:
                    tarih, konu, icerik = parts
                    notlar.append({'tarih': tarih, 'konu': konu, 'icerik': icerik})
    except FileNotFoundError:
        pass
        """
        Eğer dosyaAdi ile belirtilen dosya bulunamazsa (FileNotFoundError hatası), hata yakalanıyor ve hiçbir şey yapmadan
         geçiliyor.Böylece programın hata ile kapanması engelleniyor.
        """

def notEkle():
    konu = input("Notun konu başlığını girin: ").strip()
    if not konu:
        print("Konu boş olamaz.")
        return
    icerik = input("Notun içeriğini yazın: ").strip()
    if not icerik:
        print("İçerik boş olamaz.")
        return
    tarih = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    notlar.append({'tarih': tarih, 'konu': konu, 'icerik': icerik})
    print("Not eklendi.")

def notlariGoster():
    if not notlar:
        print("Henüz not eklenmemiş.")
        return
    print("\n--- Notlar ---")
    for i, n in enumerate(notlar, 1):
        print(f"{i}. [{n['tarih']}]")
        print(f"   Konu: {n['konu']}")
        print(f"   İçerik: {n['icerik']}\n")
    print("--------------")

def notSil():
    notlariGoster()
    try:
        secim=int(input("Silmek istediğiniz notun numarasını girin: "))
        if 1 <=secim <=len(notlar):
            #Python listeleri 0'dan başlar. O yüzden secim - 1 ile istenen notun indeksi bulunur.pop() metodu, o indeksteki notu siler ve silinen adlı değişkene atar.
            silinen= notlar.pop(secim - 1)
            print(f" '{silinen['konu']}' konusu silindi.")
        else:
            print("Geçersiz numara.")
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz.")

def notDuzenle():
    notlariGoster()
    try:
        secim= int(input("Düzenlemek istediğiniz notun numarasını girin: "))
        if 1<=secim <=len(notlar):

            eskiNot= notlar[secim-1]
            #secim - 1: Liste indeksleri 0'dan başladığı için, 1 numaralı not aslında 0. indekstedir.Seçilen not eskiNot değişkenine atanır.

            print(f"Eski Not Konusu: {eskiNot['konu']}")
            print(f"Eski Not İçeriği: {eskiNot['icerik']}")

            yeniKonu = input("Yeni konu başlığını girin (Enter ile değiştirme): ").strip()
            yeniIcerik = input("Yeni not içeriğini girin (Enter ile değiştirme): ").strip()
            if yeniKonu:
                eskiNot['konu'] = yeniKonu
            if yeniIcerik:
                eskiNot['icerik'] = yeniIcerik
            eskiNot['tarih'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")  #Not düzenlendiği için tarih güncellenir.
            print("Not güncellendi.")
        else:
            print("Geçersiz numara!!")
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")


def notAra():
    key = input("Aramak istediğiniz kelimeyi girin: ").lower()
    bulundu = False
    print("\n--- Arama Sonuçları ---")
    for i, n in enumerate(notlar, 1):
        if key in n['konu'].lower() or key in n['icerik'].lower():
            print(f"{i}. [{n['tarih']}]")
            print(f"   Konu: {n['konu']}")
            print(f"   İçerik: {n['icerik']}\n")
            bulundu = True
    if not bulundu:
        print("Aradığınız kelimeyi içeren bir not bulunamadı.")
    print("------------------------")


def notlariKaydet():
    with open(dosyaAdi, "w",encoding="utf-8") as dosya:
        for n in notlar:
            dosya.write(f"{n['tarih']}|{n['konu']}|{n['icerik']}\n")
    print("Notlar dosyaya kaydedildi.")

def menu():
    while True:
        print("\n--- Kişisel Not Defteri ---")
        print("1. Notları Göster")
        print("2. Not Ekle")
        print("3. Not Sil")
        print("4. Not Düzenle")
        print("5. Not Ara")
        print("6. Kaydet ve Çık")

        secim = input("Seçiminizi yapın (1-6): ")
        if secim == "1":
            notlariGoster()
        elif secim == "2":
            notEkle()
        elif secim == "3":
            notSil()
        elif secim == "4":
            notDuzenle()
        elif secim == "5":
            notAra()
        elif secim == "6":
            notlariKaydet()
            print("Programdan çıkılıyor...")
            print("Programdan çıkıldı.")
            break
        else:
            print("Geçersiz seçim. Lütfen 1-6 arasında bir değer girin.")

notlariYukle()
menu()