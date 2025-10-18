import qrcode
from PIL import Image

def metin_qr_donustur(metin, dosya_adi="qr_kod.png"):
    """
    Metni QR koda dönüştürür ve PNG dosyası olarak kaydeder.
    
    Parametreler:
    metin (str): QR koda dönüştürülecek metin
    dosya_adi (str): Kaydedilecek dosya adı (varsayılan: qr_kod.png)
    """
    
    # QR kod oluşturucu
    qr = qrcode.QRCode(
        version=1,  # QR kodun boyutu (1-40 arası, 1 en küçük)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Hata düzeltme seviyesi
        box_size=10,  # Her kutunun piksel boyutu
        border=4,  # Kenarlık kalınlığı (minimum 4)
    )
    
    # Metni ekle
    qr.add_data(metin)
    qr.make(fit=True)
    
    # Görüntü oluştur
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Dosyayı kaydet
    img.save(dosya_adi)
    print(f"QR kod başarıyla '{dosya_adi}' olarak kaydedildi!")
    
    return img

def renkli_qr_olustur(metin, dosya_adi="renkli_qr.png", on_renk="blue", arka_renk="yellow"):
    """
    Renkli QR kod oluşturur.
    
    Parametreler:
    metin (str): QR koda dönüştürülecek metin
    dosya_adi (str): Kaydedilecek dosya adı
    on_renk (str): QR kodun ön rengi
    arka_renk (str): QR kodun arka plan rengi
    """
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    qr.add_data(metin)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=on_renk, back_color=arka_renk)
    img.save(dosya_adi)
    print(f"Renkli QR kod başarıyla '{dosya_adi}' olarak kaydedildi!")
    
    return img


# Ana program
if __name__ == "__main__":
    print("=" * 50)
    print("QR KOD OLUŞTURUCU")
    print("=" * 50)
    
    # Kullanıcıdan metin al
    kullanici_metni = input("\nQR koda dönüştürmek istediğiniz metni girin: ")
    
    # Seçenekler
    print("\nSeçenekler:")
    print("1. Siyah-Beyaz QR Kod")
    print("2. Renkli QR Kod")
    
    secim = input("\nSeçiminiz (1 veya 2): ")
    
    if secim == "1":
        dosya_adi = input("Dosya adı girin (varsayılan: qr_kod.png): ").strip()
        if not dosya_adi:
            dosya_adi = "qr_kod.png"
        elif not dosya_adi.endswith('.png'):
            dosya_adi += '.png'
        
        metin_qr_donustur(kullanici_metni, dosya_adi)
        
    elif secim == "2":
        dosya_adi = input("Dosya adı girin (varsayılan: renkli_qr.png): ").strip()
        if not dosya_adi:
            dosya_adi = "renkli_qr.png"
        elif not dosya_adi.endswith('.png'):
            dosya_adi += '.png'
            
        on_renk = input("Ön renk (varsayılan: blue): ").strip() or "blue"
        arka_renk = input("Arka renk (varsayılan: yellow): ").strip() or "yellow"
        
        renkli_qr_olustur(kullanici_metni, dosya_adi, on_renk, arka_renk)
    
    else:
        print("Geçersiz seçim!")
    
    print("\n" + "=" * 50)
    print("Program tamamlandı!")
    print("=" * 50)