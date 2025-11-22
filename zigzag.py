import os
import time
import datetime
import random
import schedule
import msvcrt  # untuk deteksi tombol (agar scheduler bisa keluar)



# ============================================================
#                FUNGSI TAMBAHAN — ZIGZAG ANIMATION
# ============================================================

def run_zigzag():
    import time
    indent = 0
    indentIncreasing = True

    for _ in range(60):  # 60 langkah = ±6 detik
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)

        if indentIncreasing:
            indent += 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent -= 1
            if indent == 0:
                indentIncreasing = True



# ============================================================
#                     FITUR 1 – MOTIVASI
# ============================================================

def auto_motivasi():
    motivasi_list = [
        "Tetap semangat, sukses sudah menunggumu!",
        "Kamu lebih kuat dari yang kamu pikirkan!",
        "Jangan menyerah, setiap proses butuh waktu.",
        "Percaya pada diri sendiri dan terus maju!",
        "Hari ini adalah kesempatan baru untuk sukses.",
        "Langkah kecil hari ini, hasil besar besok.",
        "Kegagalan adalah bukti bahwa kamu sedang mencoba.",
        "Setiap hari adalah kesempatan baru untuk menjadi lebih baik.",
        "Yakin pada proses, bukan hanya pada hasil.",
        "Kerja keras mengalahkan bakat ketika bakat tidak bekerja keras.",
        "Fokus pada tujuan, bukan hambatan.",
        "Usaha tidak akan mengkhianati hasil.",
        "Kesuksesan dimulai dari keberanian mencoba.",
        "Kamu bisa! Jangan ragu melangkah.",
        "Tidak ada kata terlambat untuk mulai."
    ]

    motivasi_terpilih = random.sample(motivasi_list, 3)

    if not os.path.exists("motivasi"):
        os.makedirs("motivasi")

    today = datetime.date.today()
    file = f"motivasi/motivasi_{today}.txt"

    with open(file, "w", encoding="utf-8") as f:
        f.write("======= MOTIVASI HARI INI =======\n")
        f.write(f"Tanggal : {today}\n\n")
        for i, m in enumerate(motivasi_terpilih, 1):
            f.write(f"{i}. {m}\n")
        f.write("\nSemoga harimu menyenangkan! 😊")

    print(f"[FITUR 1] 3 Motivasi harian berhasil dibuat → {file}")
    run_zigzag()   # ← DITAMBAHKAN



def scheduler_motivasi():
    print("\n[INFO] Scheduler FITUR 1 berjalan... Tekan ENTER untuk berhenti.\n")
    schedule.every(5).seconds.do(lambda: [auto_motivasi(), run_zigzag()])  # ← DITAMBAHKAN

    try:
        while True:
            schedule.run_pending()
            print("[SCHEDULER] Menunggu jadwal...")
            time.sleep(1)

            if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                print("\n[INFO] Scheduler dihentikan oleh user.\n")
                break
    except KeyboardInterrupt:
        print("\n[INFO] Scheduler dihentikan (CTRL + C). Kembali ke menu.\n")



def menu_fitur1():
    while True:
        print("""
============ FITUR 1 - MOTIVASI HARIAN ============
1. Buat Motivasi Sekarang
2. Jalankan Automation
3. Kembali
""")
        p = input("Pilih menu: ")

        if p == "1":
            auto_motivasi()
        elif p == "2":
            scheduler_motivasi()
        elif p == "3":
            break
        else:
            print("Pilihan tidak valid!")



# ============================================================
#                  FITUR 2 – MONITORING FOLDER
# ============================================================

def auto_monitoring():
    folder = "."
    total = 0

    for path, dirs, files in os.walk(folder):
        for f in files:
            fp = os.path.join(path, f)
            total += os.path.getsize(fp)

    mb = round(total / (1024 * 1024), 2)

    if not os.path.exists("monitoring"):
        os.makedirs("monitoring")

    file = f"monitoring/laporan_{datetime.date.today()}.txt"

    with open(file, "w") as f:
        f.write(f"Ukuran folder saat ini: {mb} MB\n")
        f.write("STATUS: WARNING!\n" if mb > 50 else "STATUS: Normal.\n")

    print(f"[FITUR 2] Laporan monitoring dibuat → {file}")
    run_zigzag()   # ← DITAMBAHKAN



def scheduler_monitoring():
    print("\n[INFO] Scheduler FITUR 2 berjalan... Tekan ENTER untuk berhenti.\n")
    schedule.every(5).seconds.do(lambda: [auto_monitoring(), run_zigzag()])  # ← DITAMBAHKAN

    try:
        while True:
            schedule.run_pending()
            print("[SCHEDULER] Menunggu jadwal...")
            time.sleep(1)

            if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                print("\n[INFO] Scheduler dihentikan oleh user.\n")
                break
    except KeyboardInterrupt:
        print("\n[INFO] Scheduler dihentikan (CTRL + C). Kembali ke menu.\n")



def menu_fitur2():
    while True:
        print("""
============ FITUR 2 - MONITORING FOLDER ============
1. Jalankan Monitoring Sekarang
2. Jalankan Automation
3. Kembali
""")
        p = input("Pilih menu: ")

        if p == "1":
            auto_monitoring()
        elif p == "2":
            scheduler_monitoring()
        elif p == "3":
            break
        else:
            print("Pilihan tidak valid!")



# ============================================================
#                  FITUR 3 – DAILY ACTIVITY LOG
# ============================================================

def auto_dailylog():
    if not os.path.exists("daily_log"):
        os.makedirs("daily_log")

    file = f"daily_log/log_{datetime.date.today()}.txt"
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file, "a") as f:
        f.write(f"Log otomatis pada {t}\n")

    print(f"[FITUR 3] Daily Log diperbarui → {file}")
    run_zigzag()   # ← DITAMBAHKAN



def scheduler_dailylog():
    print("\n[INFO] Scheduler FITUR 3 berjalan... Tekan ENTER untuk berhenti.\n")
    schedule.every(5).seconds.do(lambda: [auto_dailylog(), run_zigzag()])  # ← DITAMBAHKAN

    try:
        while True:
            schedule.run_pending()
            print("[SCHEDULER] Menunggu jadwal...")
            time.sleep(1)

            if msvcrt.kbhit() and msvcrt.getch() == b"\r":
                print("\n[INFO] Scheduler dihentikan oleh user.\n")
                break
    except KeyboardInterrupt:
        print("\n[INFO] Scheduler dihentikan (CTRL + C). Kembali ke menu.\n")



def menu_fitur3():
    while True:
        print("""
============ FITUR 3 - DAILY ACTIVITY LOG ============
1. Buat Log Sekarang
2. Jalankan Automation
3. Kembali
""")
        p = input("Pilih menu: ")

        if p == "1":
            auto_dailylog()
        elif p == "2":
            scheduler_dailylog()
        elif p == "3":
            break
        else:
            print("Pilihan tidak valid!")



# ============================================================
#                      MENU UTAMA
# ============================================================

def main_menu():
    while True:
        print("""
============= SISTEM AUTOMATION UTS =============
1. Fitur 1 – Motivasi Harian
2. Fitur 2 – Monitoring Folder
3. Fitur 3 – Daily Activity Log
4. Keluar
""")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            menu_fitur1()
        elif pilih == "2":
            menu_fitur2()
        elif pilih == "3":
            menu_fitur3()
        elif pilih == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!")



# ============================================================
#                         MAIN
# ============================================================

if __name__ == "__main__":
    main_menu()
