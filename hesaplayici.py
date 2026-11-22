# Psikoloji Anket Puanı Hesaplayıcısı
print("Psikoloji Anket Hesaplayıcısına Hoş Geldiniz!")

# Kullanıcının adını alıyoruz (str)
ad = input("Adınızı giriniz: ")

# Kullanıcıdan üç puan alıp int türüne dönüştürüyoruz
puan1 = int(input("1. soru puanı (0-5): "))
puan2 = int(input("2. soru puanı (0-5): "))
puan3 = int(input("3. soru puanı (0-5): "))

# Toplam int, bölme sonucu ortalama float olur
toplam = puan1 + puan2 + puan3
ortalama = toplam / 3

# >= karşılaştırması bool (True / False) üretir
esik_asildi = ortalama >= 3

# f-string kullanarak biçimli çıktı oluşturuyoruz
print(f"\nKatılımcı: {ad}")
print(f"Toplam puan: {toplam}")
print(f"Ortalama puan: {ortalama:.2f}")
print(f"Eşik aşıldı mı? {esik_asildi}")
