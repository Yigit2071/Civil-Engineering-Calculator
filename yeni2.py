import tkinter as tk
from tkinter import ttk, messagebox

class DosemeHesaplamaApp:
    
    ALFA_SECENEKLER = (
        "DÖRT KENAR SÜREKLİ", "BİR KENAR SÜREKSİZ", "İKİ KOMŞU KENAR SÜREKSİZ",
        "İKİ KISA KENAR SÜREKSİZ", "İKİ UZUN KENAR SÜREKSİZ",
        "ÜÇ KENAR SÜREKSİZ", "DÖRT KENAR SÜREKSİZ"
    )

    YAN_SECENEKLER = ("KISA KENAR SÜREKSİZ", "UZUN KENAR SÜREKSİZ")
    YAN_SECENEKLER_2 = ("KISA KENAR SÜREKLİ", "UZUN KENAR SÜREKLİ")

    def __init__(self, root):
        self.root = root
        self.root.title("Döşeme Kalınlığı Hesaplama")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Döşeme Boyutları", font=("Arial", 10, "bold")).grid(row=1, column=0, columnspan=2, pady=(10, 0))

       
        """Arayüz bileşenlerini oluşturur."""
        self.create_label_entry("Uzun Kenar:", 2, "UzunKenar_entry")
        self.create_label_entry("Kısa Kenar:", 3, "KisaKenar_entry")
        self.create_label_entry("Serbest Açıklık:", 4, "SerbestAciklik_entry")

        self.create_label_entry("m Katsayısı:", 5, "m_UzunKenar_entry", button_text="m'yi Hesapla", command=self.mKatsayisi)
        self.create_label_entry("Döşemenin Çalışma Biçimi:", 6, "DosemeninCalismaBicimi_entry", entry_width=20)

        ttk.Label(self.root, text="Kenar Tipini Seçiniz:").grid(row=7, column=0)
        self.create_label_entry("Alfa (α):", 8, "AlfaS_entry")

        self.alfa_secimi = ttk.Combobox(self.root, width=27, values=self.ALFA_SECENEKLER)
        self.alfa_secimi.grid(row=7, column=1, padx=10, pady=5)
        self.alfa_secimi.set("Değeri seçiniz")
        self.alfa_secimi.bind("<<ComboboxSelected>>", self.alfa_secim_degisti)

        self.kenar_tipi_2 = ttk.Combobox(self.root, width=27, values=self.YAN_SECENEKLER)
        self.kenar_tipi_2.bind("<<ComboboxSelected>>", self.alfa_secim_degisti)

        self.kenar_tipi_3 = ttk.Combobox(self.root, width=27, values=self.YAN_SECENEKLER_2)
        self.kenar_tipi_3.bind("<<ComboboxSelected>>", self.alfa_secim_degisti)

        self.create_label_entry("hf Hesaplama:", 9, "Hfmin_entry", button_text="hf Hesapla", command=self.hf_hesapla)

    def create_label_entry(self, label_text=None, row=0, entry_name=None, entry_width=10, button_text=None, command=None):
        """Etiket ve giriş kutusunu oluşturur. Opsiyonel buton ekler."""
        ttk.Label(self.root, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky="e")
        entry = ttk.Entry(self.root, width=entry_width)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

        if button_text:
            ttk.Button(self.root, text=button_text, command=command).grid(row=row, column=2, padx=10, pady=5)
            
        setattr(self, entry_name, entry)

    def mKatsayisi(self):
        """m Katsayısını ve döşeme çalışma biçimini hesaplar."""
        try:
            uzun = float(self.UzunKenar_entry.get())
            kisa = float(self.KisaKenar_entry.get())

            if kisa <= 0 or uzun <= 0:
                raise ValueError("Uzun ve kısa kenar değerleri pozitif olmalıdır!")

            sonuc = uzun / kisa
            self.m_UzunKenar_entry.delete(0, tk.END)
            self.m_UzunKenar_entry.insert(0, str(round(sonuc, 5)))

            self.DosemeninCalismaBicimi_entry.delete(0, tk.END)
            self.DosemeninCalismaBicimi_entry.insert(0, 
                "Tek Doğrultuda Çalışan Döşeme" if sonuc > 2 else "Çift Doğrultuda Çalışan Döşeme"
            )

            return sonuc
        
        except ValueError as e:
            messagebox.showerror(title="Hata", message=str(e))
            return None

    def alfa_secim_degisti(self, event=None):
        """Alfa seçimi değiştiğinde güncelleme yapar."""
        self.AlfaS_entry.delete(0, tk.END)
        self.kenar_tipi_2.grid_forget()
        self.kenar_tipi_3.grid_forget()
        try:
            uzun = float(self.UzunKenar_entry.get())
            kisa = float(self.KisaKenar_entry.get())
            secilen_deger = self.alfa_secimi.get()

            alfa_dict = {
                "DÖRT KENAR SÜREKLİ": ((uzun * 2 + kisa * 2) / (2 * (uzun + kisa))),
                "İKİ KOMŞU KENAR SÜREKSİZ": ((uzun + kisa) / (2 * (uzun + kisa))),
                "İKİ KISA KENAR SÜREKSİZ": ((2 * uzun) / (2 * (uzun + kisa))),
                "İKİ UZUN KENAR SÜREKSİZ": ((2 * kisa) / (2 * (uzun + kisa))),
                "DÖRT KENAR SÜREKSİZ": 0
            }

            sonuc = alfa_dict.get(secilen_deger)

            if secilen_deger == "BİR KENAR SÜREKSİZ":
                self.kenar_tipi_2.grid(row=7, column=2)
                sonuc = ((uzun * 2 + kisa) / (2 * (uzun + kisa))) if self.kenar_tipi_2.get() == "KISA KENAR SÜREKSİZ" else \
                        ((uzun + kisa * 2) / (2 * (uzun + kisa)))

            elif secilen_deger == "ÜÇ KENAR SÜREKSİZ":
                self.kenar_tipi_3.grid(row=7, column=2)
                sonuc = (kisa / (2 * (uzun + kisa))) if self.kenar_tipi_3.get() == "KISA KENAR SÜREKLİ" else \
                        (uzun / (2 * (uzun + kisa)))

            if sonuc is not None:
                self.AlfaS_entry.insert(0, str(round(sonuc, 3)))
                return sonuc
            return None
        
        except ValueError:
            messagebox.showerror(title="Hata", message="Önce uzun ve kısa kenar değerlerini giriniz.")
            return None

    def hf_hesapla(self):
        """hf değerini hesaplar."""
        try:
            kisa_kenar = float(self.KisaKenar_entry.get())
            serbest_aciklik = float(self.SerbestAciklik_entry.get())
            m = self.mKatsayisi()
            alfa = self.alfa_secim_degisti()

            if alfa is None or m is None:
                return

            ls = kisa_kenar - serbest_aciklik
            hf = (ls / (15 + (20 / m))) * (1 - (alfa / 4))

            self.Hfmin_entry.delete(0, tk.END)
            self.Hfmin_entry.insert(0, str(round(hf, 3)))

        except ValueError:
            messagebox.showerror(title="Hata", message="Lütfen önce tüm değerleri giriniz.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DosemeHesaplamaApp(root)
    root.mainloop()
