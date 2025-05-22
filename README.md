📒 Kişisel Not Defteri

Bu Python uygulaması, komut satırından çalıştırılabilen basit bir kişisel not defteridir. Kullanıcı not ekleyebilir, düzenleyebilir, silebilir, arayabilir ve bu notları bir dosyada kalıcı olarak saklayabilir.

🔧 Özellikler

📌Not ekleme (başlık ve içerik ile birlikte)

📌Notları listeleme

📌Not silme

📌Not düzenleme

📌Anahtar kelime ile not arama

📌Dosyaya kaydetme ve uygulamayı kapatma

📌Uygulama başlatıldığında önceki notları otomatik yükler



📁 Dosya Yapısı

notlar.txt: Notların saklandığı dosya. Her satır şu formatta tutulur:

tarih|konu|icerik


▶️ Kullanım

Uygulama çalıştırıldığında bir menü karşınıza gelir:

--- Kişisel Not Defteri ---

1. Notları Göster

2. Not Ekle

3. Not Sil

4. Not Düzenle

5. Not Ara

6. Kaydet ve Çık


İlgili numarayı girerek işlem yapabilirsiniz.



📌 1. Notları Göster

Kayıtlı tüm notları listeler.



➕ 2. Not Ekle

Yeni bir konu ve içerik girerek not eklemenizi sağlar. Eklenen not otomatik olarak tarih damgası ile kaydedilir.



❌ 3. Not Sil

Listeyi gösterip silmek istediğiniz notun numarasını girmenizi ister.



✏️ 4. Not Düzenle

Belirli bir notun başlığını ve/veya içeriğini değiştirmenizi sağlar. Güncelleme yapıldığında tarih de yenilenir.



🔍 5. Not Ara

Girilen kelimeye göre konu veya içerikte eşleşen notları gösterir.



💾 6. Kaydet ve Çık

Notları notlar.txt dosyasına kaydeder ve programdan güvenli bir şekilde çıkış yapar.



🧠 Teknik Bilgiler

  datetime modülü: Notlara tarih damgası eklemek için kullanılır.
  
  Dosya işlemleri: open(), read(), write() fonksiyonları ile notlar dosyaya yazılır ve dosyadan okunur.
  
  Hata yönetimi: try-except blokları ile dosya bulunamadığında veya hatalı giriş yapıldığında kullanıcıya bilgi verilir.



📌 Gereksinimler

Python yüklü olmalıdır. Ekstra kütüphane gerektirmez.
