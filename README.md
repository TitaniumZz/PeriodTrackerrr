# PeriodTrackerrr

## Proje Hakkında

Period Trackerrr, regl dönemlerini takip etmeyi kolaylaştırmak için Python kullanarak geliştirdiğim basit bir komut satırı uygulamasıdır.

Bu uygulamayı yapma fikrim, regl dönemlerinin başlangıç tarihlerini, kaç gün sürdüğünü ve bu dönemdeki ruh hali değişimlerini tek bir yerde kayıt altında tutabilmekti. Böylece geçmiş kayıtlarıma kolayca bakabilir ve dönemlerim hakkında daha düzenli bir takip yapabilirim.

Uygulamayı özellikle basit ve kolay kullanılabilir tutmaya çalıştım. Herhangi bir ek Python kütüphanesi yüklemeye gerek kalmadan çalışabiliyor.

## Özellikler

Uygulamada dört farklı menü seçeneği bulunuyor:

1. **Add a period log:** Yeni bir regl kaydı ekler.
2. **Check all logs:** Daha önce eklenen bütün kayıtları gösterir.
3. **Check the last log:** En son eklenen regl kaydını gösterir.
4. **Quit:** Uygulamayı kapatır.

Yeni bir kayıt eklerken kullanıcıdan üç farklı bilgi istenir:

- Reglin başladığı tarih
- Reglin kaç gün sürdüğü
- Mood swing (ruh hali değişimi) seviyesi (1–10 arası)

Mood swing puanı ayrıca üç farklı seviyeye ayrılır:

- 1–3: Low
- 4–7: Medium
- 8–10: High

## Kullanılan Python Özellikleri

Bu projede derste öğrendiğimiz temel Python konularını kullanmaya çalıştım:

- Variables (Değişkenler)
- If / Elif / Else (Karar yapıları)
- While loops (Döngüler)
- Functions (Fonksiyonlar)
- Lists and Dictionaries (Listeler ve sözlükler)
- Try / Except (Hata kontrolü)
- File Handling (Dosya işlemleri)

Ayrıca `datetime`, `csv` ve `os` modüllerinden yararlandım.

## Girdi Kontrolleri

Uygulamanın hatalı girdilerde kapanmaması için bazı kontroller ekledim.

- Geçersiz tarih formatları kabul edilmez.
- Gelecekteki tarihler kaydedilemez.
- Regl süresi 1–15 gün arasında olmalıdır.
- Mood swing puanı 1–10 arasında olmalıdır.
- Aynı başlangıç tarihi ikinci kez kaydedilemez.
- Sayı yerine harf girildiğinde kullanıcıya uyarı gösterilir.

## Kayıt Sistemi

Eklenen regl kayıtları `period_logs.txt` isimli dosyada saklanır.

Bu sayede uygulama kapatılıp tekrar açıldığında önceki kayıtlar kaybolmaz. Program açılırken mevcut kayıtlar dosyadan okunur.

## Nasıl Çalıştırılır?

1. Python'un bilgisayarınızda kurulu olması gerekir.
2. `period_tracker.py` dosyasını bilgisayarınıza indirin.
3. Dosyayı VS Code, PyCharm veya başka bir Python editöründe açın.
4. Programı çalıştırın.
5. Ekranda çıkan menüden yapmak istediğiniz işlemi seçin.

Herhangi bir ek kütüphane kurulmasına gerek yoktur.

## Kullanılan Teknolojiler

- Python
- CSV
- Datetime
- File Handling

## Proje Amacı

Bu projeyi geliştirirken temel Python bilgilerimi gerçek hayatta kullanılabilecek küçük bir uygulamaya dönüştürmeyi amaçladım. Aynı zamanda kullanıcı girdilerini kontrol etme, verileri saklama ve fonksiyonlarla daha düzenli kod yazma konularında pratik yapmayı hedefledim.
