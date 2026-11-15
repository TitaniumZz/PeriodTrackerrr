okay so i want to make a menstrual period tracker using python for my coding literacy assignment. i was thinking of making something called "Period Trackerrr" where people can keep track of their period dates, how long their periods last and their mood swings during that time.

i want it to be a simple terminal application, nothing too complicated. when the program starts i want it to show a menu like this:

```python
print("\n Period Trackerrr")
print("1. Add a period log")
print("2. Check all logs")
print("3. Check the last log")
print("4. Quit")
```

for the first option, i want the user to enter 3 things:
- the date their period started (day.month.year format)
- how many days their period lasted
- their mood swing level during that period, rated from 1 to 10

for the mood swing part, i want the program to automatically describe the score as low, medium or high. something like 1-3 being low, 4-7 medium and 8-10 high.
the second option should show all the previous period logs with their dates, duration and mood swing scores. i want the newest records to show up first.
the third option should only show the latest period log. and obviously if there aren't any records yet, it should tell the user that instead of giving an error.
i also want the records to actually stay saved after closing the program, so i was thinking of using a txt file called period_logs.txt. when the user opens the program again, it should load the previous records automatically.

i don't want the program to crash whenever someone enters something wrong either. for example, if they enter an impossible date like 32.04.2026, a date in the future, letters instead of numbers or a mood swing score outside 1-10, it should show a warning and let them try again. the same goes for period duration, which should only accept numbers between 1 and 15. it should also prevent users from entering the same period start date twice.

i need the code to include the things we've learned in class, like variables, if/elif/else, while loops, functions, lists or dictionaries and file handling. i also need at least 3 functions and some try/except statements for error handling.

i'm still learning python, so don't make the code unnecessarily advanced or complicated. i want to understand what each part does because i might have to explain it to my teacher. try to keep the code organized and add comments where they're actually needed.

once you write the code, explain the functions to me and help me come up with test examples so i can check if everything works, including some wrong inputs.

i basically want it to look like a small but properly working period tracking application, while still keeping it suitable for a beginner python assignment.

Prompt:

bu ödevi python kullanarak bir regl takvimi uygulaması yapmak istiyorum. bana ödevin yönergelerine uygun bi kod oluşturabilir misin? çok karmaşık olmasın çünkü kodu kendim de anlayabilmem ve sunarken anlatabilmem gerekiyor. terminal üzerinden çalışan basit bi uygulama olsun.

Kararım: AI'nın oluşturduğu temel uygulama fikrini kabul ettim. Ama kodun çok karışık olmamasına ve ödevdeki bütün gereksinimleri karşılamasına dikkat ettim.

2. Kullanıcıdan alınacak bilgilerin değiştirilmesi

Prompt:

uygulamanın kullanıcıdan alacağı bilgiler biraz daha belirli olsun istiyorum. regl başlangıç tarihini, reglin kaç gün sürdüğünü ve o günkü mood swing seviyesini 1-10 arasında sorsun. bunlar dışında ekstra bi şey sormasına gerek yok.

Kararım: Bu öneriyi kabul ettim. Uygulamayı daha basit tutmak için yalnızca bu üç bilgiyi kullanmaya karar verdim.

3. Kodun ödev gereksinimlerine uygunluğunun kontrol edilmesi

Prompt:

bu ödevimin gereksinimlerini karşılıyo dimi? yönergede istenen en az 3 input, if else kullanımı, loop, function ve dosyaya kaydetme gibi şeyler kodda var mı kontrol eder misin? eksik bi şey varsa söyle.

Kararım: AI'nın kontrol etmesini istedim çünkü sadece çalışan bir kod değil, hocanın istediği teknik gereksinimleri de karşılayan bir ödev hazırlamam gerekiyordu. Eksik olabilecek noktaları kontrol ederek kodu geliştirmeye karar verdim.

4. Hatalı kullanıcı girişlerinin kontrol edilmesi

Prompt:

kullanıcı yanlış bi tarih girerse veya gün sayısı yerine harf yazarsa program kapanmasın istiyorum. yanlış giriş yaptığında uyarı versin ve tekrar sorsun. aynı şekilde mood swing için de sadece 1-10 arasında sayı girilebilsin. bunu kodda düzgün bi şekilde ayarlayabilir misin?

Kararım: Bu öneriyi kabul ettim. Kullanıcının yanlış giriş yapmasının programı bozmaması benim için önemliydi. Bu yüzden tarih, gün sayısı ve mood swing girişlerine kontrol ekledim.

5. README dosyasının hazırlanması

Prompt:

github'a koymak için bi readme hazırlamam gerekiyor. uygulamanın ne yaptığını, nasıl çalıştırılacağını ve özelliklerini anlatsın. çok resmi veya aşırı profesyonel yazma lütfen, benim yazmışım gibi basit ve anlaşılır türkçe olsun. kodda kullandığım şeyleri de kısaca açıklasın.

Kararım: AI'nın hazırladığı README taslağını kullandım ancak dilinin çok resmi olmamasına dikkat ettim. Uygulamayı gerçekten nasıl yaptığımı ve hangi özelliklere sahip olduğunu anlatan bir dosya olmasını istedim.
