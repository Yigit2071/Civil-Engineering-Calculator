import tkinter as tk
from tkinter import ttk


class DosemeHesaplamaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DÖŞEME KALINLIĞI HESAPLAMA")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        """Arayüz bileşenlerini oluşturur."""

        # Kenar Tipi
        ttk.Label(self.root, text="Kenar Tipi:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.KenarTipi_entry = ttk.Entry(self.root, width=20)
        self.KenarTipi_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        # Döşeme Boyutları Başlığı
        ttk.Label(self.root, text="Döşeme Boyutları", font=("Arial", 10, "bold")).grid(
            row=1, column=0, columnspan=2, pady=(10, 0)
        )

        # Uzun Kenar ve Kısa Kenar
        self.create_label_entry("Uzun Kenar:", 2, "UzunKenar_entry")
        self.create_label_entry("Kısa Kenar:", 3, "KisaKenar_entry")
        self.create_label_entry("Serbest Açıklık:", 4, "SerbestAciklik_entry")

        # m Katsayısı ve Döşeme Çalışma Biçimi
        self.create_label_entry("m =", 5, "m_UzunKenar_entry", button_text="m'yi Hesapla", command=self.mKatsayisi)
        self.create_label_entry("Döşemenin Çalışma Biçimi:", 6, "DosemeninCalismaBicimi_entry", entry_width=20)

        # Alfa (α) Hesaplama
        self.create_label_entry("α =", 7, "AlfaS_entry", button_text="α'yı Hesapla")

        # hf Hesaplama
        self.create_label_entry("hf =", 8, "Hfmin_entry", button_text="hf Hesapla")

    def create_label_entry(self, label_text, row, entry_name, entry_width=10, button_text=None, command=None):
        """Etiket ve giriş kutusunu oluşturur. Opsiyonel buton ekler."""
        ttk.Label(self.root, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky="e")

        entry = ttk.Entry(self.root, width=entry_width)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="ew")

        if button_text:
            button = ttk.Button(self.root, text=button_text, command=command)
            button.grid(row=row, column=2, padx=10, pady=5)

        setattr(self, entry_name, entry)  # Değişkenleri koruyarak atama yapar.

    def mKatsayisi(self):
        """m Katsayısını ve döşeme çalışma biçimini hesaplar."""
        self.DosemeninCalismaBicimi_entry.delete(0,tk.END)
        self.m_UzunKenar_entry.delete(0,tk.END)
        try:
            uzun = float(self.UzunKenar_entry.get())
            kisa = float(self.KisaKenar_entry.get())

            if kisa <= 0 or uzun <= 0 :
                self.m_UzunKenar_entry.delete(0, tk.END)
                self.DosemeninCalismaBicimi_entry.delete(0, tk.END)
                raise ValueError("Kısa Kenar sıfır olamaz!")
                
            sonuc = uzun / kisa
            self.m_UzunKenar_entry.delete(0, tk.END)
            self.m_UzunKenar_entry.insert(0, str(round(sonuc, 5)))

            # Döşeme Çalışma Biçimi Belirleme
            self.DosemeninCalismaBicimi_entry.delete(0, tk.END)
            if sonuc > 2:
                self.DosemeninCalismaBicimi_entry.insert(0, "Tek Doğrultuda Çalışan Döşeme")
            else:
                self.DosemeninCalismaBicimi_entry.insert(0, "Çift Doğrultuda Çalışan Döşeme")

        except ValueError as e:
            print("Hata:", e)
            self.UzunKenar_entry.delete(0,tk.END)
            self.KisaKenar_entry.delete(0,tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = DosemeHesaplamaApp(root)
    root.mainloop()
