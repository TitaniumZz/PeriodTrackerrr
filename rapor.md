# Period Trackerrr – Süreç Raporu

**GEP1316 Kodlama Okuryazarlığı | Ara Değerlendirme Ödevi 1**

**Öğrenci:** Lalin İpek Ersoy  
**Okul Numarası:** 2365121  
**Proje:** github.com/TitaniumZz/PeriodTrackerrr

## Problem ve kullanıcı

Period Trackerrr, regl başlangıç tarihini, reglin kaç gün sürdüğünü ve ruh hâli değişimini düzenli olarak kaydetmek isteyen kişiler için yaptığım basit bir Python uygulaması. Bazen bu tarz bilgileri farklı notlara yazmak veya eski kayıtları bulmaya çalışmak biraz uğraştırıcı olabiliyor. Ben de bütün bu bilgilerin tek bir yerde tutulabileceği küçük bir uygulama yapmak istedim.

Uygulama aslında oldukça basit çalışıyor. Kullanıcı menüden yeni bir kayıt ekleyebiliyor, daha önce girdiği bütün kayıtları görebiliyor veya sadece son kaydına bakabiliyor. Kayıtlar `period_logs.txt` dosyasına kaydedildiği için program kapatılıp tekrar açıldığında da bilgiler kaybolmuyor.

Uygulamayı 2030 senaryosunda, kişisel sağlık takibini kolaylaştırmaya yönelik basit bir kayıt aracı olarak düşündüm. Program herhangi bir teşhis koymuyor veya gelecekteki regl tarihini tahmin etmiyor. Sadece kullanıcının kendi girdiği bilgileri saklıyor.

## Tasarım ve sözde kod

Uygulamayı hazırlarken önce nasıl çalışmasını istediğime karar verdim. Çok fazla özellik eklemek yerine, kullanımı kolay bir menü oluşturmayı tercih ettim.

Programın genel çalışma mantığı şöyle:

1. Program açıldığında daha önce kaydedilmiş bilgiler okunuyor.
2. Kullanıcıya seçeneklerin olduğu bir menü gösteriliyor.
3. Kullanıcı yeni kayıt eklemek isterse regl başlangıç tarihi, kaç gün sürdüğü ve mood swing puanı soruluyor.
4. Yanlış veya geçersiz bir bilgi girilirse program hata vermek yerine uyarı gösterip tekrar giriş istiyor.
5. Bilgiler geçerliyse kaydediliyor.
6. Kullanıcı isterse bütün kayıtlarını veya en son kaydını görebiliyor.
7. Çıkış seçildiğinde program kapanıyor.

## Yapay zekâ ile çalışma günlüğü

Projeyi yaparken ChatGPT'den özellikle kodu oluşturma, bazı bölümleri düzenleme ve ödev gereksinimlerini kontrol etme konusunda yardım aldım. Kullandığım promptların detaylı hâli GitHub reposundaki `PROMPTLAR.md` dosyasında bulunuyor.

**1. Uygulamanın oluşturulması**

İlk olarak Python kullanarak basit bir regl takvimi uygulaması yapmak istediğimi söyledim. Terminal üzerinden çalışan, menüsü olan ve çok karmaşık olmayan bir program hazırlamasını istedim.

**Kararım:** Temel uygulama fikrini kabul ettim. Özellikle kodu kendim de anlayabilmek ve sunum sırasında anlatabilmek istediğim için gereksiz karmaşık özellikler eklememeye karar verdim.

**2. Kullanıcıdan alınacak bilgilerin belirlenmesi**

Daha sonra uygulamanın hangi bilgileri sorması gerektiğini netleştirdim. Regl başlangıç tarihi, reglin kaç gün sürdüğü ve mood swing seviyesinin 1-10 arasında puanlanmasını istedim.

**Kararım:** Bu üç bilgiyi kullanmaya karar verdim. Daha fazla soru eklemek yerine uygulamanın temel amacına odaklanmasını istedim.

**3. Ödev gereksinimlerinin kontrol edilmesi**

Kodun ödev yönergesinde istenen şartları karşılayıp karşılamadığını kontrol etmesini istedim. Özellikle input, if/else, loop, function ve dosyaya kayıt gibi konuların kullanılıp kullanılmadığına baktık.

**Kararım:** Sadece kodun çalışmasının yeterli olmadığını fark ettim. Ödevde istenen diğer dosyaların, testlerin ve raporun da hazırlanması gerektiğini göz önünde bulundurdum.

**4. Hatalı girişlerin kontrol edilmesi**

Kullanıcı yanlış tarih girerse veya sayı yerine harf yazarsa programın direkt kapanmasını istemedim. Bunun yerine hata mesajı gösterip tekrar giriş yapmasını sağlayacak kontroller eklenmesini istedim.

**Kararım:** Bu öneriyi kabul ettim. Kullanıcının yanlış bir bilgi girmesi durumunda programın çalışmaya devam etmesini önemli buldum. Bu yüzden tarih, süre ve mood swing puanı için doğrulamalar kullandım.

**5. README dosyasının hazırlanması**

Son olarak GitHub reposuna eklemek için uygulamayı ve özelliklerini anlatan bir README dosyası hazırlamasını istedim. Çok resmi bir dil yerine daha basit ve anlaşılır Türkçe kullanmasını özellikle belirttim.

**Kararım:** README'nin uygulamanın gerçekten ne yaptığını anlatmasına dikkat ettim. Kullanım şeklini, özelliklerini ve kodda kullandığım temel konuları ekledim.

## Test ve hata ayıklama

Uygulamayı denerken hem normal girişler hem de yanlış girişler kullandım. Amacım, kullanıcının yanlış bir şey yazdığında programın kapanmaması ve doğru bilgi girene kadar tekrar sormasıydı.

Aşağıdaki sonuçlar paylaştığım terminal ekran görüntülerindeki denemelere dayanmaktadır.

| Girdi / İşlem | Beklenen sonuç | Gerçek sonuç |
|---|---|---|
| Menüye 5 yazılması | Hata mesajı gösterilmesi | Uyarı verildi ve menü tekrar gösterildi. |
| Tarih olarak 19.13.2026 yazılması | Geçersiz tarihin reddedilmesi | Tarih kabul edilmedi ve tekrar soruldu. |
| Süre olarak 0 yazılması | 1-15 aralığı dışında olduğu için reddedilmesi | Aralık uyarısı gösterildi. |
| Süre yerine harf yazılması | Sayı girilmesinin istenmesi | Tam sayı uyarısı gösterildi. |
| Mood swing olarak 11 yazılması | 1-10 aralığı dışında olduğu için reddedilmesi | Aralık uyarısı gösterildi. |
| 15.11.2026, 4 gün ve 5 puan girilmesi | Yeni kaydın eklenmesi | Kayıt eklendi ve mood seviyesi Medium olarak gösterildi. |
| Menüden 2 ve 3 seçeneklerinin seçilmesi | Bütün kayıtların ve son kaydın gösterilmesi | Eklenen kayıt iki ekranda da görüntülendi. |
<img width="395" height="193" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (5)" src="https://github.com/user-attachments/assets/911217ce-d719-4b82-ba25-ab1660190c89" />
<img width="390" height="153" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (4)" src="https://github.com/user-attachments/assets/4de18c4d-c681-4e30-a676-c884c63654b1" />
<img width="388" height="51" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (3)" src="https://github.com/user-attachments/assets/41090cad-1978-4846-a5cb-b44aaa3d3320" />
<img width="377" height="104" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (2)" src="https://github.com/user-attachments/assets/3981fc12-a72a-48cc-9389-ce38ece3a81a" />
<img width="342" height="197" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (1)" src="https://github.com/user-attachments/assets/22a4a4b5-b3b6-4bb9-b8ae-4e3955f3eea6" />
<img width="322" height="335" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM" src="https://github.com/user-attachments/assets/b0b8eb56-5e2a-4cca-95a8-1430db046db2" />
<img width="518" height="349" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (9)" src="https://github.com/user-attachments/assets/e129eb21-8dd1-4194-83d4-20fe7c091945" />
<img width="577" height="427" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (8)" src="https://github.com/user-attachments/assets/050c72f7-053e-4686-9247-26cd4735cac5" />
<img width="488" height="267" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (7)" src="https://github.com/user-attachments/assets/eda012bf-d334-4ef0-8f35-9f3e6c8558b1" />
<img width="446" height="202" alt="WhatsApp Image 2026-11-15 at 8 57 21 PM (6)" src="https://github.com/user-attachments/assets/b7c8013e-c370-4192-9f81-2731a543236e" />


## Hata örneği ve değerlendirme

Kod üzerinde çalışırken dosyadan kayıtları okuma kısmının da doğru çalışmasının önemli olduğunu fark ettim. Önceki sürümde bozuk satırların atlanması veya dosya okunamadığında programın boş bir listeyle devam etmesi gibi durumlar olabiliyordu. Bu da bazı kayıtlar kaybolmuş gibi görünmesine rağmen programın normal çalıştığı izlenimini verebilirdi.

Bu yüzden güncel sürümde dosyanın başlığını ve kayıtların içeriğini kontrol eden doğrulamalar bulunuyor. Dosyada bir sorun varsa program kullanıcıya uyarı veriyor ve normal şekilde devam etmiyor. Böylece kayıtların eksik veya yanlış okunması ihtimalini azaltmış oldum.

## Kişisel yansıtma

Bu projeyi yaparken aslında küçük bir uygulama oluşturmanın bile düşündüğümden daha fazla aşaması olduğunu gördüm. İlk başta sadece kullanıcıdan birkaç bilgi alan basit bir regl takvimi yapmak istiyordum. Ancak daha sonra bu bilgilerin nasıl saklanacağı, kullanıcı yanlış giriş yaptığında ne olacağı ve program tekrar açıldığında eski kayıtların nasıl gösterileceği gibi detayları da düşünmem gerekti.

Python'da kullandığımız konuları uygulama üzerinde görmek benim için daha anlaşılır oldu. Özellikle fonksiyonların her işlemi ayrı ayrı düzenlemeye yardımcı olduğunu fark ettim. Liste ve sözlük kullanarak kayıtları tutmak, döngülerle menüyü tekrar göstermek ve if/else yapılarıyla farklı durumları kontrol etmek projenin temel parçalarıydı. Dosyaya kayıt yapma kısmı da öğrendiğim konuları gerçek bir örnekte kullanmamı sağladı.

Yapay zekâdan bu süreçte oldukça fazla yardım aldım. Ama verdiği her cevabı direkt doğru kabul etmek yerine kodu çalıştırıp kontrol etmem gerektiğini de öğrendim. Özellikle yanlış tarih ve geçersiz sayı girişleriyle yaptığım denemeler, programın gerçekten istediğim gibi çalışıp çalışmadığını görmemi sağladı.

Bence bu projeden öğrendiğim en önemli şey, bir uygulama yaparken sadece ana özelliğin çalışmasının yeterli olmadığı. Kullanıcının yapabileceği hataları da düşünmek ve programı farklı durumlarda denemek gerekiyor. İleride oyun geliştirme veya başka yazılım projelerinde de bu yaklaşımın işime yarayacağını düşünüyorum.

## Yapay zekâ kullanım beyanı ve kaynakça

**Kullanılan araç:** ChatGPT

**Kullanım amacı:** Kod oluşturma, kodu düzenleme, hata kontrolü, test sürecine yardımcı olma ve rapor hazırlama.

Bu projede yapay zekâdan destek aldım. Ancak oluşturulan kodları ve metinleri kendi projemin ihtiyaçlarına göre kontrol ettim ve düzenledim. Teslim ettiğim çalışmanın içeriğinden ve doğruluğundan kendim sorumluyum.

**Ad Soyad:** Lalin İpek Ersoy  
**Okul Numarası:** 2365121  
**Tarih:** 15.11.2026  

**Kaynakça**
OpenAI. (2026). *ChatGPT* [Büyük dil modeli]. https://chatgpt.com
