import csv
import os
from datetime import datetime, date

# Kayitlar bu dosyada saklanir.
FILE_NAME = "period_logs.txt"


def load_logs():
    """Kayitlari okur. Bozuk dosya varsa None dondurur."""
    logs = []

    if not os.path.exists(FILE_NAME):
        return logs

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            # Bos dosya yeni bir kayit dosyasi gibi kullanilabilir.
            if reader.fieldnames is None and os.path.getsize(FILE_NAME) == 0:
                return logs

            # Baslik bozuksa ekleme yapmak eski kayitlari okunamaz hale getirir.
            if reader.fieldnames != ["start_date", "duration", "mood_swing"]:
                raise ValueError("Dosya basligi gecersiz")

            kayitli_tarihler = set()

            for row in reader:
                if None in row:
                    raise ValueError("Satirda fazladan alan var")

                start_date = datetime.strptime(
                    row["start_date"], "%Y-%m-%d"
                ).date()
                duration = int(row["duration"])
                mood_swing = int(row["mood_swing"])

                if start_date > date.today():
                    raise ValueError("Gelecekteki bir tarih kayitli")
                if not 1 <= duration <= 15:
                    raise ValueError("Regl suresi 1-15 disinda")
                if not 1 <= mood_swing <= 10:
                    raise ValueError("Mood swing puani 1-10 disinda")
                if start_date in kayitli_tarihler:
                    raise ValueError("Tekrar eden tarih kayitli")

                kayitli_tarihler.add(start_date)
                logs.append({
                    "start_date": start_date,
                    "duration": duration,
                    "mood_swing": mood_swing
                })

    except (OSError, csv.Error, UnicodeError, KeyError, TypeError, ValueError):
        print("Hata: Kayit dosyasi bozuk veya okunamiyor.")
        print("Verileri korumak icin program baslatilmadi. Dosyayi kontrol et.")
        return None

    return logs


def save_log(log):
    """Yeni regl kaydini period_logs.txt dosyasina ekler."""
    file_is_new = not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_is_new:
            writer.writerow(["start_date", "duration", "mood_swing"])

        writer.writerow([
            log["start_date"].strftime("%Y-%m-%d"),
            log["duration"],
            log["mood_swing"]
        ])


def get_start_date(existing_logs):
    """Kullanicidan gecerli ve tekrar etmeyen bir baslangic tarihi alir."""
    while True:
        date_text = input("Reglinin basladigi tarih (GG.AA.YYYY): ").strip()

        try:
            start_date = datetime.strptime(date_text, "%d.%m.%Y").date()

            if start_date > date.today():
                print("Uyari: Gelecekteki bir tarihi kaydedemezsin. Tekrar dene.")
            elif any(log["start_date"] == start_date for log in existing_logs):
                print("Bu tarih zaten kayitli. Baska bir tarih gir.")
            else:
                return start_date

        except ValueError:
            print("Gecersiz tarih! Ornek format: 15.11.2026")


def get_number(prompt, min_value, max_value):
    """Belirlenen aralikta bir tam sayi girilene kadar kullaniciya sorar."""
    while True:
        value = input(prompt).strip()

        try:
            number = int(value)

            if min_value <= number <= max_value:
                return number
            else:
                print(f"Lutfen {min_value} ile {max_value} arasinda bir sayi gir.")

        except ValueError:
            print("Lutfen harf veya baska bir karakter degil, tam sayi gir.")


def get_mood_description(mood_swing):
    """Mood swing puanini okunabilir bir aciklamaya cevirir."""
    if mood_swing <= 3:
        return "Low - Ruh hali degisimi az"
    elif mood_swing <= 7:
        return "Medium - Orta duzeyde ruh hali degisimi"
    else:
        return "High - Yogun ruh hali degisimi"


def add_period(logs):
    """Kullanicidan uc bilgi alir, yeni kaydi listeye ve dosyaya ekler."""
    print("\n--- New Period Log ---")

    start_date = get_start_date(logs)
    duration = get_number("Reglin kac gun surdu? (1-15): ", 1, 15)
    mood_swing = get_number(
        "O donemde mood swing seviyen nasildi? (1-10, 10 en yogun): ",
        1, 10
    )

    new_log = {
        "start_date": start_date,
        "duration": duration,
        "mood_swing": mood_swing
    }

    try:
        save_log(new_log)
        logs.append(new_log)
        print("\nRegl kaydin basariyla eklendi!")
        print("Mood swing seviyesi:", get_mood_description(mood_swing))
    except OSError:
        print("Dosyaya kayit yapilamadi. Dosya konumunu kontrol et.")


def show_logs(logs):
    """Butun kayitlari en yeniden en eskiye dogru ekrana yazdirir."""
    print("\n--- All Period Logs ---")

    if len(logs) == 0:
        print("Henuz hic kayit eklemedin.")
        return

    sorted_logs = sorted(logs, key=lambda log: log["start_date"], reverse=True)

    for number, log in enumerate(sorted_logs, start=1):
        print(f"\nKayit {number}")
        print("Regl baslangic tarihi:",
              log["start_date"].strftime("%d.%m.%Y"))
        print("Regl suresi:", log["duration"], "gun")
        print("Mood swing puani:", str(log["mood_swing"]) + "/10")
        print("Mood swing seviyesi:",
              get_mood_description(log["mood_swing"]))


def show_last_log(logs):
    """En son regl kaydini ekrana yazdirir."""
    print("\n--- Last Period Log ---")

    if len(logs) == 0:
        print("Henuz hic kayit eklemedin.")
        return

    last_log = max(logs, key=lambda log: log["start_date"])

    print("Regl baslangic tarihi:",
          last_log["start_date"].strftime("%d.%m.%Y"))
    print("Regl suresi:", last_log["duration"], "gun")
    print("Mood swing puani:", str(last_log["mood_swing"]) + "/10")
    print("Mood swing seviyesi:",
          get_mood_description(last_log["mood_swing"]))


def main():
    """Ana menu: kullanicinin sectigi islemi tekrar tekrar calistirir."""
    logs = load_logs()

    if logs is None:
        return

    print("\n==============================")
    print("       PERIOD TRACKERRR")
    print("==============================")

    while True:
        print("\n1. Add a period log")
        print("2. Check all logs")
        print("3. Check the last log")
        print("4. Quit")

        choice = input("\nWhat would you like to do? (1-4): ").strip()

        if choice == "1":
            add_period(logs)
        elif choice == "2":
            show_logs(logs)
        elif choice == "3":
            show_last_log(logs)
        elif choice == "4":
            print("Period Trackerrr kullandigin icin tesekkurler. Byee!")
            break
        else:
            print("Gecersiz secim! Lutfen 1, 2, 3 veya 4 gir.")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nGiris kesildi. Program guvenli sekilde kapatildi.")
