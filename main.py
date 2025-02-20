import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("DÖŞEME KALINLIĞI HESAPLAMA")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# insaat_photo = tk.PhotoImage(file="C:/Users/SINERJIPC/Desktop/insaatHesapMak/Baret.png")
# resized_image = insaat_photo.subsample(5,5)
# image_label = tk.Label(image=insaat_photo)
# image_label.grid(row=0,column=0)

#Functions
def mKatsayisi():
    m_UzunKenar_entry.delete(0,tk.END)
    DosemeninCalismaBicimi_entry.delete(0,tk.END)
    try:
        uzun = int(UzunKenar_entry.get())
        kisa = int(KisaKenar_entry.get())
        sonuc = uzun/kisa
        m_UzunKenar_entry.insert(0,str(round(sonuc,5)))
        if sonuc > 2:
            DosemeninCalismaBicimi_entry.insert(0,"Tek Doğrultu da çalışan döşeme")
        else:
            DosemeninCalismaBicimi_entry.insert(0,"Çift Doğrultu da çalışan döşeme")
    except:
        UzunKenar_entry.delete(0,tk.END)
        KisaKenar_entry.delete(0,tk.END)
        
#Label and Entry
ttk.Label(root, text="Kenar Tipi:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
KenarTipi_entry = ttk.Entry(root, width=20)
KenarTipi_entry.grid(row=0, column=1, padx=10, pady=5)

# Döşeme Boyutu Başlık
ttk.Label(root, text="Döşeme Boyutları", font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=2, pady=(10, 0))

# Uzun ve Kısa Kenar
ttk.Label(root, text="Uzun Kenar:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
UzunKenar_entry = ttk.Entry(root, width=10)
UzunKenar_entry.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Kısa Kenar:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
KisaKenar_entry = ttk.Entry(root ,width=10)
KisaKenar_entry.grid(row=3, column=1, padx=10, pady=5)

# Serbest Açıklık
ttk.Label(root, text="Serbest Açıklık:").grid(row=4, column=0, padx=10, pady=5, sticky="e")
SerbestAciklik_entry = ttk.Entry(root, width=10)
SerbestAciklik_entry.grid(row=4, column=1, padx=10, pady=5)

# m Katsayısı
ttk.Label(root, text="m =").grid(row=5, column=0, padx=10, pady=5, sticky="e")
m_UzunKenar_entry = ttk.Entry(root, width=10)
m_UzunKenar_entry.grid(row=5, column=1, padx=10, pady=5)
m_button = ttk.Button(root, text="m'yi Hesapla", command=mKatsayisi)
m_button.grid(row=5, column=2, padx=10, pady=5)

# Döşeme Çalışma Biçimi
ttk.Label(root, text="Döşemenin Çalışma Biçimi:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
DosemeninCalismaBicimi_entry = ttk.Entry(root, width=20)
DosemeninCalismaBicimi_entry.grid(row=6, column=1, padx=10, pady=5)

# AlfaS (α) Hesaplama
ttk.Label(root, text="α =").grid(row=7, column=0, padx=10, pady=5, sticky="e")
AlfaS_entry = ttk.Entry(root, width=10)
AlfaS_entry.grid(row=7, column=1, padx=10, pady=5)
AlfaS_button = ttk.Button(root, text="α'yı Hesapla")
AlfaS_button.grid(row=7, column=2, padx=10, pady=5)

# hf Hesaplama
ttk.Label(root, text="hf =").grid(row=8, column=0, padx=10, pady=5, sticky="e")
Hfmin_entry = ttk.Entry(root, width=10)
Hfmin_entry.grid(row=8, column=1, padx=10, pady=5)
Hfmin_button = ttk.Button(root, text="hf Hesapla")
Hfmin_button.grid(row=8, column=2, padx=10, pady=5)

root.mainloop()